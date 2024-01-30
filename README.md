# AI Tools Telegram Bot

Welcome to the AI Tools Telegram Bot, your personal assistant for creating AI-generated art, enhancing images, and more! This Telegram bot leverages the power of various AI models to perform tasks like generating art from text prompts, high-resolution image restoration, colorizing black and white photos, removing backgrounds, and describing the content of images.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Commands](#commands)
- [Contributing](#contributing)
- [Contact](#contact)
- [License](#license)

## Features

1. **Create AI Art (Text To Image):** Generate stunning AI art from text prompts.
2. **Robust Face Restoration:** Restore old photos with a robust face restoration algorithm.
3. **Add Colors to Old Images:** Colorize black and white photos to bring them to life.
4. **Remove Photo Backgrounds:** Effortlessly remove backgrounds from photos.
5. **Visual Description AI:** Get a detailed description of the content of an image.

## Installation

To use the AI Tools Telegram Bot, follow these installation steps:

1. Install the required Python libraries:
    ```bash
    pip install pyrogram==2.0.106 replicate asyncio requests
    ```

2. Get your API tokens:
    - Main API ID and API Hash from [my.telegram.org/apps](https://my.telegram.org/apps)
    - Bot token from [@BotFather](https://t.me/BotFather)
    - Replicate API token from [Replicate](https://replicate.com)

3. Set environment variables:
    ```bash
    export REPLICATE_API_TOKEN="your_replicate_api_token"
    ```

4. Update the API configurations in the script with your obtained tokens.

5. Run the script:
    ```bash
    python bot.py
    ```

## commands

Start the bot and use the following commands to interact with it:

- `/art [prompt]`: Create AI art from a text prompt.
- `/resolution`: Enhance the resolution of a photo (Reply to a photo).
- `/colorize`: Add colors to a black and white photo (Reply to a photo).
- `/removebg`: Remove the background of a photo (Reply to a photo).
- `/describe`: Get a detailed description of the content of a photo (Reply to a photo).

## Contributing

Contributions are welcome! Feel free to open issues or pull requests to improve the functionality or fix any bugs.

## Contact

<a href="https://t.me/LampStack">Telegram</a><br>
<a href="mailto:xialop@outlook.com">Email</a>

## License

This project is licensed under the [MIT License](LICENSE).
