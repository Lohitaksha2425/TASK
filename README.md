# Application Dockerization

This project contains a `Dockerfile` that provides instructions to build a Docker image for the application. The image includes all necessary configurations to run the application in a containerized environment.

## Building the Docker Image

DockerImage was built using the following command:

```sh
docker build -t 21bce5501_analysis .
```

## Tagging and Pushing the Docker Image

DockerImage was tagged using the following command:

```sh
docker tag 21bce5501_analysis:latest lohitaksha2425/21bce5501_analysis:latest
```

This command was used to create a copy of the image with the name `lohitaksha2425/21bce5501_analysis:latest`, making it ready to be pushed.

DockerImage was pushed to the repository using the following command:

```sh
docker push lohitaksha2425/21bce5501_analysis:latest
```

## Usage

To download and run the Docker image for this Flask application, follow these steps:

1. **Pull the Docker image**:

    ```sh
    docker pull lohitaksha2425/21bce5501_analysis:latest
    ```

2. **Run the Docker container**:

    ```sh
    docker run -p 5000:5000 lohitaksha2425/21bce5501_analysis:latest
    ```

3. **Access the application**:

    Open a web browser and visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to view the Flask application.
