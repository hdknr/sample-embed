{% load fullurl %}
(function(){
  'use strict';

  // 目印のaタグからパラメータとってきたら消す
  var atag = document.getElementsByClassName('widget-embed');
  var username = atag[0].dataset.ghUsername;
  atag[0].style.display = 'none';     // anchor を見えなくする

  // <iframe>を作成
  var iframe = document.createElement('iframe');
  iframe.scrolling = 'no';
  iframe.frameBorder = 0;
  iframe.marginWidth = 0;
  iframe.marginHeight = 0;
  iframe.width = '100%';
  iframe.height = '180px';
  iframe.id = 'article-widget-frame';

  // atagの隣にiframeを挿入
  atag[0].parentNode.insertBefore(iframe,atag[0]);

  var req = new XMLHttpRequest();
  req.onreadystatechange = function() {
    if (req.readyState == 4) { // 通信の完了時
      if (req.status == 200) { // 通信の成功時
          var doc = iframe.contentWindow.document;
          doc.open();
          doc.write(req.responseText);
          doc.close();
      }
    }
  }
  req.open('GET', '{% fullurl view.handlers.detail id=instance.id tpl="widget" %}');
  req.send(null);
})();
