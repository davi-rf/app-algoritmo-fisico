var Prism = (function () {
  var _ = (self.Prism = {
    languages: {
      python: {
        comment: { pattern: /#.*/, greedy: true },
        string: {
          pattern:
            /("""[\s\S]*?"""|'''[\s\S]*?'''|("|')(?:\\.|(?!\2)[^\\\r\n])*\2)/,
          greedy: true
        },
        keyword:
          /\b(and|as|assert|break|class|continue|def|del|elif|else|except|False|finally|for|from|global|if|import|in|is|lambda|None|nonlocal|not|or|pass|raise|return|True|try|while|with|yield)\b/,
        number: /\b\d+(\.\d+)?\b/,
        function: /\b[a-zA-Z_]\w*(?=\()/,
        operator: /[-+%=]=?|!=|<=?|>=?|\*\*?|\//,
        punctuation: /[{}[\];(),.:]/
      }
    },
    highlightAll: function () {
      document
        .querySelectorAll('code[class*="language-"]')
        .forEach(function (el) {
          var code = el.textContent
          var html = code
            .replace(/(&)/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')

          Object.keys(_.languages.python).forEach(function (type) {
            var rule = _.languages.python[type]
            html = html.replace(rule.pattern, function (m) {
              return '<span class="token ' + type + '">' + m + '</span>'
            })
          })

          el.innerHTML = html
        })
    }
  })
  return _
})()
