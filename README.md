# DARE
Dynamic Application Rotation Environment for Moving Target Defense (MTD)

## Documentation
[comments](https://demo.hedgedoc.org/WgeztfZzSk27-Uic5WKIQQ?both)

[article](https://www.overleaf.com/project/6290ef1fb8b577a786ca5821)

Django REST API documentation:

https://www.django-rest-framework.org/


Creating migration:
* python manage.py makemigrations
* python manage.py migrate


Installation:
* pip install django
* pip install djangorestframework


To run a server:
* python manage.py runserver
* python manage.py runserver 82

Enable ip / port forwarding:
* https://jensd.be/1086/linux/forward-a-tcp-port-to-another-ip-or-port-using-nat-with-nftables

Apache server setup:
* https://www.digitalocean.com/community/tutorials/apache-basics-installation-and-configuration-troubleshooting
* https://www.guru99.com/apache.html
* https://serverfault.com/questions/1077204/nftables-loopback-connections-not-working-in-centos-7

VM port forwarding
* https://www.howtogeek.com/122641/how-to-forward-ports-to-a-virtual-machine-and-use-it-as-a-server/
* https://stackoverflow.com/questions/9537751/virtualbox-port-forward-from-guest-to-host

Prerouting and postrouting:
* https://unix.stackexchange.com/questions/457375/local-port-forwarding-using-iptables-is-not-working

Nginx
* https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-server-blocks-virtual-hosts-on-ubuntu-16-04

Wordpress
* https://www.tecmint.com/install-wordpress-with-nginx-in-ubuntu-20-04/

Change wordpress siteurl from mysql:
* a
* use mysite;
* select * from wp_options where option_name like 'siteurl';
* select * from wp_options where option_name like 'home';
* change value if you wish


Change ports for servers:
* https://www.linuxshelltips.com/change-wordpress-port-apache-nginx/



### Efficiency tests:
Execute test:
```
python single_client_efficiency_test.py --url "http://localhost:8080" --requests-count 5000 --results-path "single_client_eff_results_1.csv"
```

Plot results:
```
python create_plot_for_efficiency_test.py --results-path "single_client_eff_results_1.csv" --plot-path "plots/single_client_eff_plot_1.png"
```
