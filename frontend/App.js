import {
  View,
  Text,
  Image,
  StyleSheet,
  Alert,
  TouchableOpacity,
  StatusBar,
  Platform
} from 'react-native'

import { useState, useEffect } from 'react'
import * as ImagePicker from 'expo-image-picker'

export default function App() {
  const [image, setImage] = useState(null)

  useEffect(() => {
    if (Platform.OS === 'web') return
    ;(async () => {
      const cam = await ImagePicker.requestCameraPermissionsAsync()
      const lib = await ImagePicker.requestMediaLibraryPermissionsAsync()

      if (cam.status !== 'granted' || lib.status !== 'granted') {
        Alert.alert('Permissões necessárias')
      }
    })()
  }, [])

  const selectImage = async () => {
    const result = await ImagePicker.launchImageLibraryAsync({
      mediaTypes: ImagePicker.MediaTypeOptions.Images
    })

    if (!result.canceled) {
      setImage(result.assets[0].uri)
    }
  }

  const openCamera = async () => {
    const result = await ImagePicker.launchCameraAsync()

    if (!result.canceled) {
      setImage(result.assets[0].uri)
    }
  }

  return (
    <View style={styles.container}>
      <StatusBar
        barStyle='light-content'
        backgroundColor='#000'
      />

      <Text style={styles.title}>Imagem (Expo)</Text>

      {Platform.OS === 'web' ? (
        <TouchableOpacity
          style={styles.btn}
          onPress={selectImage}
        >
          <Text style={styles.btnText}>Selecionar foto</Text>
        </TouchableOpacity>
      ) : (
        <View style={styles.row}>
          <TouchableOpacity
            style={styles.btn}
            onPress={selectImage}
          >
            <Text style={styles.btnText}>Fototeca</Text>
          </TouchableOpacity>
          <TouchableOpacity
            style={styles.btn}
            onPress={openCamera}
          >
            <Text style={styles.btnText}>Câmera</Text>
          </TouchableOpacity>
        </View>
      )}

      {image && (
        <Image
          source={{ uri: image }}
          style={styles.image}
        />
      )}
    </View>
  )
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#000',
    padding: 20,
    gap: 12
  },
  title: {
    marginTop: 40,
    color: '#fff',
    fontSize: 20,
    alignSelf: 'center'
  },
  row: {
    flexDirection: 'row',
    width: '100%'
  },
  btn: {
    backgroundColor: '#1760ff',
    padding: 12,
    borderRadius: 8,
    flex: 1,
    marginHorizontal: 5,
    alignItems: 'center'
  },
  btnText: {
    color: '#fff',
    fontWeight: 'bold'
  },
  image: {
    width: '100%',
    height: 280,
    borderRadius: 8
  }
})
