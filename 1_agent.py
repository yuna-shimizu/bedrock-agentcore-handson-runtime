# 必要なライブラリをインポート
from strands import Agent

# エージェントを作成
agent = Agent("jp.anthropic.claude-sonnet-4-5-20250929-v1:0")

# エージェントを起動
agent("Strandsってどういう意味？")
