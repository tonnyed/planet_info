# Planet Information Assessment 

This is a Python program that provides information about planets in our solar system. It includes a Tkinter GUI, unit tests, and input validation.

## Features
- Display planet details (name, mass, distance from the Sun, and moons).
- Query planets by name.
- Input validation to ensure valid planet names are entered.

## How to Run
1. Clone the repository.
2. Navigate to the project folder:
   ```bash
   cd planet_info
3. Build the Docker Image.
   Once you have your Dockerfile, you can build the image with the following command:
   ```bash
   docker build -t tonnyed/plannet-app .
4. Run the Docker Container with GUI Access.
   Running Tkinter in a Docker container requires displaying the GUI on the host system.
   This step depends on your operating system:
````
For Linux:
You can run the container with access to the X server (the system that handles GUI display).
````
  
   ```bash
   docker run -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix tonnyed/plannet-app
-e DISPLAY=$DISPLAY: 
   ````

This sets the DISPLAY environment variable to the host system's display.
-v /tmp/.X11-unix:/tmp/.X11-unix: This mounts the X11 Unix socket,
which allows the container to use the display on the host.
Make sure to allow Docker containers to access your X server with the following
command on Linux (if necessary):



# For macOS:
To run graphical applications in Docker on macOS,
you would need to use an X11 server like XQuartz.

Now, run the Docker container with the following command:
brew cask install xquartz or
`https://github.com/XQuartz/XQuartz/releases/download/XQuartz-2.8.5/XQuartz-2.8.5.pkg`

    ```bash
    brew install socat
    open -a XQuartz
    ```
After installing, start XQuartz and then enable access to your display with:
   ```bash
   socat TCP-LISTEN:6000,reuseaddr,fork UNIX-CLIENT:\"$DISPLAY\"
   ```
# in another window
   ```bash
   docker run -e DISPLAY=host.docker.internal:0 tonnyed/plannet-app
   ```

# For Windows:
For Windows, you would need an X server to display the GUI, such as VcXsrv.
After installing and running VcXsrv, follow similar steps as on macOS,
setting DISPLAY=host.docker.internal:0.

5. Run Your Python Tkinter Application.
   Once you have the container running, the Tkinter GUI should appear on your host system's display.
   Your application should behave as if it's running locally on your machine.