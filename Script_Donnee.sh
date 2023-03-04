#curl https://www.google.com/finance/quote/.INX:INDEXSP?hl=fr > /home/ec2-user/Projet_Linux_Python/Code_Source_Site.txt

curl https://www.google.com/finance/quote/ADA-EUR?hl=fr > /home/ec2-user/Projet_Linux_Python/Code_Source_Site.txt
current_time=$(date +"%Y-%m-%d %T")
var=$(cat /home/ec2-user/Projet_Linux_Python/Code_Source_Site.txt | grep -oP '(?<="YMlKec fxKbKc">)[^<]+' | tr ',' '.')
echo $var
echo $current_time
echo "$current_time,$var" >> /home/ec2-user/Projet_Linux_Python/Prix.csv
