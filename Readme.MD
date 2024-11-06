# Setting up Docker Hub, WebApp with Private Repo, and GitHub Deployment

This guide provides steps to:
1. Create a Docker Hub profile and Personal Access Token (PAT).
2. Configure a private Docker container repository for a WebApp.
3. Set up GitHub as a deployment source with SCM authentication.
4. Optionally, set up a webhook from Docker for automated updates.

---

## Prerequisites
- A Docker Hub account
- A GitHub account
- Access to Azure for creating and configuring WebApps

---

## Step 1: Create Docker Hub Profile and Generate a PAT

1. **Sign up or Log in to Docker Hub**:
   - Go to [Docker Hub](https://hub.docker.com/) and sign in or create a new account.

2. **Generate a Personal Access Token (PAT)**:
   - Navigate to **Account Settings** > **Security**.
   - Click on **New Access Token**.
   - Provide a name for the token, generate it, and save it securely. This token will be used for authentication in place of your password.

![Docker Hub Security Settings](image.png)

---

## Step 2: Configure the WebApp with a Private Docker Repository

1. **Create a WebApp in Azure**:
   - Go to Azure and start creating a new WebApp.

2. **Configure the Container Settings**:
   - In the WebApp creation settings, select the **Container** option.
   - Choose **Private Repository** as the repository type.
   - Enter your Docker Hub **Image Name** (e.g., `username/repository-name`).

3. **Authenticate with Docker Hub**:
   - Enter your Docker Hub **Username** and **PAT** from Step 1 to allow the WebApp to pull the image.

![WebApp Container Configuration](image-1.png)

---

## Step 3: Set Up GitHub Deployment with SCM Authentication

1. **Go to the Deployment Center**:
   - After creating the WebApp, navigate to the **Deployment Center** in the Azure portal.

2. **Select GitHub as the Deployment Source**:
   - Choose **GitHub** as the source for continuous deployment.

3. **Enable SCM Authentication**:
   - When prompted, enable **SCM authentication**. This will allow secure GitHub integration for automated deployments.

---

## Optional: Set Up a Docker Webhook for Automatic Updates

1. **Create a Webhook in Docker Hub**:
   - Go to your repository in Docker Hub.
   - Navigate to **Webhooks** and set up a new webhook to trigger automatic deployments when the container image is updated.

![Docker Webhook Setup](image-2.png)

---

By following these steps, you will have a Docker Hub private repository integrated with an Azure WebApp, with GitHub set up as the deployment source. Additionally, you can automate updates via Docker webhooks if desired.
