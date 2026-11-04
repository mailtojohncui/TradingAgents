import sys

from tradingagents.default_config import DEFAULT_CONFIG
from tradingagents.graph.trading_graph import TradingAgentsGraph

ticker = sys.argv[1] if len(sys.argv) > 1 else "META"
date = sys.argv[2] if len(sys.argv) > 2 else "2026-11-02"

ta = TradingAgentsGraph(debug=False, config=DEFAULT_CONFIG.copy())
final_state, decision = ta.propagate(ticker, date)
print(decision)
print(ta.save_reports(final_state, ticker))
