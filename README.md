# contributter-ranking-bot

contributterを使っているユーザーの1日のcontribute数トップ3をメンション付きで自動ツイートするbotです。

実際のbot:https://twitter.com/_who_is_king

詳細記事:https://zenn.dev/shuntatakemoto/articles/00264c2b366612



### 処理機構
①昨日の#contributter_reportのついたツイート内のcontribution数とユーザーIDを取得

②contribution数を集計してランキング化

③ランキング上位3人をメンションしてcontribution数を記載し、自動ツイート

### 使用技術

Python,Twitter API,cron
