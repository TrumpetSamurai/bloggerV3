BloggerAPI V3 をPythonで使うサンプル  

1 pip install --upgrade google-api-python-client  
  pip install oauth2client  

2 Google APIs ConsoleからBlogger APIの有効化及び、認証情報タブから認証情報を作成で、OAuth 2.0認証に必要なclient ID、client secretの取得(client_id.jsonをdownloadして同じdirectoryにおく)

3 35行目　blog_get_obj = blogs.get(blogId='ブログID')　にブログIDを設定

4 実行したらブラウザが開き、認証したら文字列がでるので、19行目 auth_code = 'ブラウザに表示された文字列をここに貼り付ける' に貼り付ける

5 再度実行すると、credentials.datができるので、これを使って認証できる