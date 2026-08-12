# VS Code and Python Installation Setup

## 1. Install VS Code

Download and install Visual Studio Code from:

https://code.visualstudio.com/download

## 2. Install Python

Download and install Python from:

https://www.python.org/downloads/

> **Tip:** During Python installation on Windows, make sure to select **Add Python to PATH**.

## 3. Create a Virtual Environment

Create a Python virtual environment in your project folder:

```cmd
python -m venv .venv
```

## 4. Activate the Virtual Environment

In the VS Code terminal, activate your virtual environment:

```cmd
.venv\Scripts\activate
```

> **Note:** Replace `.venv` with your actual virtual environment folder name if it is different.

After activation, you should see something similar to:

```text
(.venv) C:\YourProject>
```

## 5. Install the Python Extension in VS Code

1. Open **VS Code**.
2. Click the **Extensions** icon on the left sidebar.
3. Search for **Python**.
4. Select **Python by Microsoft**.
5. Click **Install** if it is not already installed.

## 6. Verify Python Installation

Run the following command in the VS Code terminal:

```cmd
python --version
```

Verify that Python is installed correctly.

You can also verify the virtual environment:

```cmd
where python
```

The output should point to your project's `.venv` directory.


# GitHub Setup and First Repository

## 7. Create and Set Up Your GitHub Project

### Phase 1: Create Your GitHub Account

#### 1. Visit the GitHub Website

Open your browser and navigate to the official GitHub website:

https://github.com/

#### 2. Start Sign-Up

Click the **Sign up** button located in the top-right corner of the page.

#### 3. Enter Your Credentials

Provide:

* A valid email address
* A strong password

#### 4. Choose a Username

Pick a unique username.

> **Note:** Your username will be publicly visible on your GitHub projects.

#### 5. Verify Humanity

Complete the verification puzzle to confirm that you are a human user.

#### 6. Confirm Your Email

Retrieve the verification code sent to your email inbox and enter it in the browser window.

#### 7. Select a Plan

Skip the personalization survey if desired and select the **GitHub Free** plan to get started.

---

### Phase 2: Create Your First Project (Repository)

Once your GitHub dashboard loads, create your first project repository.

#### 1. Open the New Repository Form

Click the **New** button on the left sidebar.

Alternatively:

* Click the **+** icon in the top-right corner.
* Select **New repository**.

#### 2. Name the Project

Enter a short and memorable name in the **Repository name** field.

Example:

```text
my-first-project
```

#### 3. Add a Description

Enter a brief summary of your project in the optional **Description** field.

Example:

```text
My first Python project
```

#### 4. Set Repository Visibility

Choose one of the following:

* **Public** — Anyone can view your code.
* **Private** — Only authorized users can access your repository.

#### 5. Initialize the Repository

Select:

```text
Add a README file
```

This creates an introductory `README.md` file for your project.

#### 6. Create the Repository

Scroll to the bottom and click the green:

**Create repository**

button.

---

### Phase 3: Add Files to Your Project

#### 1. Open the Upload Menu

On your new repository page:

* Click **Add file**.
* Select **Upload files**.

#### 2. Select Your Files

Drag and drop your project files from your computer directly into the GitHub browser window.

For example:

```text
my-first-project/
├── app.py
├── requirements.txt
└── README.md
```

#### 3. Commit the Changes

Scroll down to the **Commit changes** section.

Enter a short description of what you added.

Example:

```text
Added initial Python project files
```

Click:

**Commit changes**

Your files are now saved in your GitHub repository.

---

## Next Step

You can continue by learning either:

1. **Git Command Line** — Connect your GitHub repository to your computer using Git commands.
2. **GitHub Desktop** — Manage your repository using a graphical desktop application without needing to use Git commands.


