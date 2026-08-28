# Step-by-Step Guide: Install Ollama and Pull Qwen 0.5B

Here is a step-by-step guide to installing Ollama and pulling the Qwen 0.5B model. Since you need to take screenshots for your assignment, the steps where you should capture your screen are highlighted.

## Phase 1: Install Ollama

### For Windows
1. Go to the official website: [https://ollama.com/download](https://ollama.com/download).
2. Click on the **Download for Windows** button to get the `OllamaSetup.exe` file.
3. Run the downloaded file and follow the on-screen installation prompts.
4. Once finished, Ollama will run in the background. 

> 📸 **Screenshot 1:** Take a screenshot of the Ollama installation window or the completed installation success screen.

### For macOS
1. Go to [https://ollama.com/download](https://ollama.com/download).
2. Click on **Download for macOS**.
3. Open the downloaded `.zip` file and drag the **Ollama** app into your **Applications** folder.
4. Open the app from your Applications folder to start the Ollama service.

> 📸 **Screenshot 1:** Take a screenshot of the Ollama app in your Applications folder or the initial launch screen.

### For Linux
1. Open your terminal.
2. Run the official installation script by typing the following command and pressing Enter:
   ```bash
   curl -fsSL https://ollama.com/install.sh | sh

---
### Phase 2: Verify the Installation

Before pulling the model, ensure Ollama is installed correctly.

1. Open your command line interface:
   * **Windows:** Open Command Prompt or PowerShell.
   * **macOS/Linux:** Open Terminal.
2. Type the following command and press Enter:
   ```bash
   ollama --version
---

### Phase 3: Pull the Qwen 0.5B Model
Now you will download the model to your local machine.
In the same Command Prompt or Terminal window, type the following command to pull the latest 0.5B Qwen model (Qwen 2.5):

   ```bash
   ollama pull qwen2.5:0.5b
   ollama run qwen2.5:0.5b
---
