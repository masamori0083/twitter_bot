# twitter_bot
Pythonライブラリを使用して作成したbotプログラム。画像をテキスト付きで投稿できます。

### 使用した API,ライブラリ
---
- Twitter Developer API
- tweepy ref:https://docs.tweepy.org/en/latest/index.html


### tweepy について
---
使用したメソッド

- tweepy.OAuth1UserHandler
  - API 認証を行うメソッド
    - https://docs.tweepy.org/en/latest/authentication.html
- tweepy.API
  - 認証を渡して、twitter API の各メソッド（エンドポイント）を呼び出す
    - https://docs.tweepy.org/en/latest/api.html#tweepy.API
- API.update_status_with_media()
  - API POST status/update_with_media を呼び出す
    - https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-statuses-update_with_media
