<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <title>恭喜，您的服务器已经能正常使用ASP.NET！</title>
    <style>
        .container {
            width: 60%;
            margin: 10% auto 0;
            background-color: #f0f0f0;
            padding: 2% 5%;
            border-radius: 10px
        }

        ul {
            padding-left: 20px;
        }

            ul li {
                line-height: 2.3
            }

        a {
            color: #20a53a
        }
    </style>
</head>
<body>
    <div class="container">
      <h1>恭喜，您的服务器已经能正常使用ASP.NET！</h1>
        <ul>
            <li>本页面基于Mono:5.20.1.27&nbsp;Jexus:6.1.30编译</li>
            <li>当前时间:<%=DateTime.Now.ToString()%></li>
            <li>更多功能了解，请查看<a href="https://www.bt.cn/bbs/thread-33593-1-1.html" target="_blank">ASP.NET 兼容插件</a></li>
          <li>Copyright 2019© <a href="https://www.iw3c.top">iw3c.top iw3c.cc</a></li> 
        </ul>
    </div>
   <script type="text/javascript">
      var port=window.location.port;
      if(port!="2333") window.location.href="404.1.html";
  </script>
</body>
</html>
