# D'abord on vient récuperer le code source du site de google finance et le met dans un fichier text
curl https://www.google.com/finance/quote/ADA-EUR?hl=fr > /home/ec2-user/Projet_Linux_Python/Code_Source_Site.txt

# On récupere ensuite la date et l'heure à un instant T
current_time=$(date +"%Y-%m-%d %T")

# On vient récupérer la donnée avec regrex 
# https://regexr.com/79mgb
# (?<= balise )[^<]+ va récuperer tous les caractères après la balise, or il n'y a que le prix
# De plus, vu qu'on va devoir faire un csv, je remplace la , par un . car la virgule en csv permet de séparer les colonne 
var=$(cat /home/ec2-user/Projet_Linux_Python/Code_Source_Site.txt | grep -oP '(?<="YMlKec fxKbKc">)[^<]+' | tr ',' '.')
# echo $var
# echo $current_time

# ensuite on met les 2 variables dans un fichier csv
echo "$current_time,$var" >> /home/ec2-user/Projet_Linux_Python/Prix.csv
