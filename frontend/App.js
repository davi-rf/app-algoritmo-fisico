import {
  View,
  Text,
  Image,
  StyleSheet,
  TouchableOpacity,
  ScrollView,
  ActivityIndicator,
  Modal,
  Dimensions,
  Platform
} from 'react-native'

import { useState } from 'react'
import * as ImagePicker from 'expo-image-picker'
import { WebView } from 'react-native-webview'

const API_URL = 'http://SEU_IP_AQUI:8000/processar'

export default function App() {
  const [image, setImage] = useState(null)
  const [codigo, setCodigo] = useState('')
  const [saida, setSaida] = useState('')
  const [loading, setLoading] = useState(false)
  const [zoom, setZoom] = useState(false)

  const enviarImagem = async uri => {
    setLoading(true)
    setCodigo('')
    setSaida('')

    const form = new FormData()
    form.append('file', {
      uri,
      name: 'image.png',
      type: 'image/png'
    })

    const res = await fetch(API_URL, {
      method: 'POST',
      body: form
    })

    const json = await res.json()
    setCodigo(json.codigo)
    setSaida(json.saida)
    setLoading(false)
  }

  const pickImage = async (camera = false) => {
    const result = camera
      ? await ImagePicker.launchCameraAsync()
      : await ImagePicker.launchImageLibraryAsync()

    if (!result.canceled) {
      const uri = result.assets[0].uri
      setImage(uri)
      enviarImagem(uri)
    }
  }

  return (
    <ScrollView style={styles.container}>
      <Text style={styles.title}>Algoritmo Físico</Text>

      <View style={styles.row}>
        {Platform.OS !== 'web' && (
          <TouchableOpacity
            style={styles.btn}
            onPress={() => pickImage(true)}
          >
            <Text style={styles.btnText}>Câmera</Text>
          </TouchableOpacity>
        )}
        <TouchableOpacity
          style={styles.btn}
          onPress={() => pickImage(false)}
        >
          <Text style={styles.btnText}>Galeria</Text>
        </TouchableOpacity>
      </View>

      {image && (
        <TouchableOpacity onPress={() => setZoom(true)}>
          <Image
            source={{ uri: image }}
            style={styles.image}
          />
        </TouchableOpacity>
      )}

      {loading && (
        <ActivityIndicator
          size='large'
          color='#1760ff'
        />
      )}

      {codigo !== '' && (
        <>
          <Text style={styles.label}>Código Python</Text>

          <View style={styles.codeBox}>
            <WebView
              originWhitelist={['*']}
              source={{
                uri: 'file:///android_asset/prism.html',
                baseUrl: ''
              }}
              injectedJavaScript={`
                document.getElementById('code').textContent = ${JSON.stringify(codigo)};
                Prism.highlightAll();
              `}
              style={{ height: 300 }}
            />
          </View>

          <Text style={styles.label}>Saída</Text>
          <Text style={styles.output}>{saida}</Text>
        </>
      )}

      <Modal
        visible={zoom}
        transparent
      >
        <View style={styles.modal}>
          <Image
            source={{ uri: image }}
            style={styles.fullImage}
            resizeMode='contain'
          />
          <TouchableOpacity
            style={styles.close}
            onPress={() => setZoom(false)}
          >
            <Text style={styles.btnText}>Fechar</Text>
          </TouchableOpacity>
        </View>
      </Modal>
    </ScrollView>
  )
}

const styles = StyleSheet.create({
  container: { flex: 1, padding: 20, backgroundColor: '#000' },
  title: { color: '#fff', fontSize: 22, textAlign: 'center', marginBottom: 12 },
  row: { flexDirection: 'row', gap: 10 },
  btn: { flex: 1, backgroundColor: '#1760ff', padding: 14, borderRadius: 10 },
  btnText: { color: '#fff', fontWeight: 'bold', textAlign: 'center' },
  image: { width: '100%', height: 260, marginTop: 12, borderRadius: 10 },
  label: { color: '#fff', marginTop: 16, marginBottom: 6, fontWeight: 'bold' },
  codeBox: { backgroundColor: '#111', borderRadius: 8, overflow: 'hidden' },
  output: {
    backgroundColor: '#1c1c1c',
    color: '#fff',
    padding: 12,
    borderRadius: 8
  },
  modal: {
    flex: 1,
    backgroundColor: 'rgba(0,0,0,0.95)',
    justifyContent: 'center'
  },
  fullImage: {
    width: Dimensions.get('window').width,
    height: Dimensions.get('window').height * 0.85
  },
  close: {
    backgroundColor: '#1760ff',
    padding: 14,
    margin: 20,
    borderRadius: 10
  }
})
