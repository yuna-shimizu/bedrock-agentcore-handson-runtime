# 必要なライブラリをインポート
from strands import Agent

# エージェントを作成
agent = Agent("us.amazon.nova-2-lite-v1:0")

# エージェントを起動
agent("Strandsってどういう意味？")
