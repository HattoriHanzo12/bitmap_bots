# Bitmap Cats 🐾

Welcome to **Bitmap Cats**, a novel project that transforms Bitcoin block data into unique, generative cat NFTs! By parsing block data from the [Bitmap](https://bitmap.io/) protocol using the Blockstream API, this project creates pixel-art cats with traits mapped to block attributes like transaction count, block size, and timestamp. Each cat is a one-of-a-kind digital collectible, ready to be minted as an NFT using UniSat.

## �� How It Works

Bitmap Cats leverages the uniqueness of Bitcoin blocks to generate pixel-art cats:
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

Each cat is unique because each Bitcoin block is unique—making Bitmap Cats a fun and innovative way to create digital collectibles tied to the blockchain!

## 🛠️ Getting Started

### Prerequisites
- **Python 3.13**
