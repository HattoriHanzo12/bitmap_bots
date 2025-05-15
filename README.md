# Bitmap Bots 🤖

Welcome to **Bitmap Bots**, a novel project that transforms Bitcoin block data into unique, generative bot NFTs! By parsing block data from the [Bitmap](https://bitmap.io/) protocol using the Blockstream API, this project creates pixel-art bots with traits mapped to block attributes like transaction count, block size, and timestamp. Each bot is a one-of-a-kind digital collectible, ready to be minted as an NFT using UniSat.

## 🎨 How It Works

Bitmap Bots leverages the uniqueness of Bitcoin blocks to generate pixel-art bots:
- **Block Data**: We fetch data for a given block height (e.g., `800000`) using the [Blockstream API](https://blockstream.info/api).
- **Trait Mapping**:
  - **Colors**: The block hash is hashed again to map vibrant colors (cyan, magenta, lime, etc.) to body parts like the head, body, ears, paws, tail, and nose.
  - **Head Size**: Determined by the block size (larger blocks = larger heads).
  - **Spots**: The number of spots is based on the transaction count (`tx_count`).
  - **Collar**: A red collar appears if the scaled transaction count exceeds a threshold.
  - **Ear Shape**: The block timestamp determines whether ears are upright or folded.
  - **Eyes and Pupils**: Eyes have mapped colors, with black pupils for visibility.
- **Image Generation**: Using Python and the Pillow library, we generate 300x300 pixel-art images for each block.
- **Minting**: The generated images can be inscribed as NFTs on the Bitcoin blockchain using [UniSat](https://unisat.io/) via the Ordinals protocol.

## 🛠️ Getting Started

### Running the Script
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/bitmap_bots.git
   cd bitmap_bots
2. **Set Up the Virtual Environment**:
   ```bash
   /usr/local/bin/python3.13 -m venv venv
   source venv/bin/activate

   Using the App
Option 1: Generate and View a Single Bot (Wallet-Integrated Version)
This version of the app allows you to connect to UniSat Wallet, generate a bot, and attempt to mint it directly (though manual inscription is recommended due to API limitations).
Step 1: Open the App
Open the index.html file in a web browser:
Right-click index.html in your file explorer and select "Open with" > your browser.

Alternatively, in VSCode, use the "Live Server" extension to run the app locally.

You’ll see the Bitmap Bots interface with a title, input field, and buttons ("Connect UniSat Wallet", "Generate Bot", "Mint as NFT").
Step 2: Generate a Bot
Input a Block Height:
Enter a Bitcoin block height in the input field (e.g., 1130).

This should be a block height for which you own the corresponding Bitmap inscription (e.g., 1130.bitmap).

Connect UniSat Wallet:
Click "Connect UniSat Wallet" and follow the prompts to connect your wallet.

This step verifies ownership of the Bitmap inscription (see "Verifying Ownership" below).

Generate the Bot:
Click "Generate Bot".

The app will fetch block data from Blockstream’s API and generate a unique bot image based on the block height.

The bot will be displayed on the canvas below the buttons, along with a status message like "Bot generated for Bitmap 1130!".

Step 3: Prepare for Minting
The "Mint as NFT" button attempts to mint the bot using window.unisat.inscribe, but this may fail due to API limitations.

Instead, download the bot image for manual inscription:
Right-click the canvas and select "Save image as..." to download the bot as a PNG (e.g., bitmap-bot-1130.png).
![Example](bot_1130.png)



Proceed to the "Minting a Bot Manually" section below.

