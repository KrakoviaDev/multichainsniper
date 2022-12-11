# multichainsniper
Multi chain and multi wallet sniper that works on a variety of decentralized exchanges as well.

## Interested in buying?
Message me on telegram!
- [Telegram](https://t.me/non_linear_logic)


### Supported chains and exchanges
- Ethereum
    - Uniswap
    - Sushiswap

- Binance smart chain
    - Pancakeswap
    - Sushiswap
    - Apeswap
    - Backeryswap

- Polygon Matic
    - Quickswap
    - Apeswap
    - Defyn

- Kucoin Community Chain
    - Kuswap
    - KoffeSwap

- Okex Chain
    - CherrySwap

- Avalanche Mainnet C-Chain
    - Pangolin
    - Trader Joe

- Fantom Opera
    - Spirit Swap
    - Spooky Swap
    - Protofi

- Cronos Mainnet beta
    - Meerkat
    - VVS Finance
    - Cronaswap

- Harmony chain shard 0
    - Viper

- Metis Andromeda Mainnet
    - Netswap
    - Tethys


### Innovative UI
The bot has a UI which runs in the terminal, this allows you to run the bot on remote servers without needing a display server or having to play with virtual displays as you would with normal UIs.

![Loading screen](https://i.imgur.com/Rave54x.png)
![Working screen](https://i.imgur.com/Kl8FY6u.png)

### Current features
- Multi wallet support
- Support for custom pairs (Tokens that are paired to a different coin than the default one of the exchange)
- Instant buy functionality, you can make the bot Instantly skipping it's normal flow in case something changes after you've started it.
- Automatically detect owner, max buy, trading open functions and sell triggering functions (ex. mint, blacklist and so on)
- Mempool scan for liquidity scanning & trading open scanning
- Option to send multiple buy transactions at the same time (99% all get in the same block at relatively near positions from each other, depends also on the node you use)
- Honeypot prevention, you can set the bot to check if the token is a honeypot before buying.
- Max buy tax and max sell tax prevention, the bot will only sell if the current tax is below the amount you set.
- Anti-bot prevention, options to skip blocks/seconds after liquidity detection, option to skip blocks/seconds after trading enable detection, minimum liquidity check (to be added in v1.0.1) 
- Anti rug

### Changelogs

#### Version 1.0.0
- Initial release
- Added TUI (Text user interface), it's like GUI but you can run your bot in the terminal)
- Added support for multiple wallets
- Added automatic trading enable function detection
- Added automatic bad functions (sell triggering) detection
- Added automatic owner address detection
- Improved mempool speed and overall performance
- Improved sending transactions speed
- Option to change secondary wallets on your own

#### Version 1.0.1
- Fix small bugs from version 1.0.0
- Add option to set gas price and gas limit also from UI rather than config only
- Add netswap and Tethys on Metis chain

#### Version 1.0.2
- Support for ethereum chain and it's new gas system
- Support for buying exact amount of tokens
- Add missing chains and exchanges
- Fix bugs from version 1.0.1

#### Version 1.0.3
- Add rug pull prevention (sell when liquidity is about to be removed or when a bad function is about to be called on the token contract)
- Add option to scroll the token functions table at startup screen
- Add IPC node connection support
- Added anti rug system
- Improvements to mempool scan

#### version 1.1.0
- Implement minimum liquidity option
- Add everything related to selling the tokens, sell certain % of tokens, certain amounts of tokens. Sell based on take profit and stop loss


#### version 1.2.0
- Telegram scrapper added (features in telegram)


#### version 1.3.0
- Contract buy mode added (anti blacklist)
- You will have to deploy a contract on each corresponding chain!
