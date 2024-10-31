#### Setting Up

##### Installing packages

- Install the following in GNU/Linux:

    ```
    flite alsa-libs alsa-tools alsa-utils pulseaudio-alsa vlc
    ```

    also install python package named poetry:
    ```
    pip3 install poetry
    ``` 


- For Fedora only:
  
    ```
    sudo dnf install flite alsa-libs alsa-tools alsa-utils pulseaudio-alsa
    pip3 install poetry
    ```

    Install VLC through flatpak in software otherwise VLC gives broken audio

---

##### Configuration

- Edit the config_example.json after giving required data place it in a folder named Nova in your home directory.

---

##### Installing and Running it

Then to install and run it, run these commands in the cloned directory. 

```
poetry install
poetry run nova
```

