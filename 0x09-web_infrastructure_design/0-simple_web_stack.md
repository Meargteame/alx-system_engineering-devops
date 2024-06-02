Description 
This is a simple web infrastructure that hosts a website that is reachable via www.foobar.com. There are no firewalls or SSL certificates for protecting the server's network. Each component (database, application server) has to share the resources (CPU, RAM, and SSD) provided by the server.


What is a server
· A server is a computer system that provides resources, services, or data to
other computers (clients) over a network.
In this case, our server hosts the web infrastructure components.

What is the role of the domain name
The role of domain name is just for remembering the name only because humans can't remember
different numberes that are allocated for specific website or what not .
so instead of the numbers which is the ip adress ,
some good persons gave us this system.

What type of DNS record www is in www.foobar.com

- on our case we are using the CNAME record , because the "www.foobar.com" is subdomain of the main domain "foobar.com" so that the "www.foobar.com" is just another canonical name for the same webspage ,because the "www.foobar.com" is also locating for the same destination

What is the role of the web server

- the WEB SERVER , I like to call the web server "watchman of house" because it watches everything that comes to
  the sever before any other of the server components .
- the webserver is responsible for the accepting http requestes sent from the client or the user and it replies if it can like if it is website it responds the simple files like HTML ,CSS , JAVASCRIPT FILES
- and if not it will give the request to the application server.

What is the role of the application server

- the role of application server is appling or executing the application , so we have the codebsae or the application files and application server executes with the need of what it is asked for .
- it do it's work by communicating with the web sever to return a dynamic personalized response to the client request

What is the role of the database

- this is where actually the data persists.
  -it stores and manipulates the structured data of the website .

What is the server using to communicate with the computer of the user requesting the website

- when the user requests the website www.foobar.com , their computer sends an HTTP request over the internet .
- after several traveling the request it reaches our server "8.8.8.8" .
- then the server responds with the requested web content ,
- then it will be displayed on the user's web browser.

Issues with the Infrastructure:

- SPOF (single point of failure) :
  if you look at our infrastructure it only have one server , which is really not good . because it makes it vulnerable to downtime .

  - if the server failes there is nothing else the website can not accessed so it have this issue of only having one server

- Downtime when maintenance needed:
  this issue is also not good because as a rule when maintennace is needed or like deploying new code web server needs to be restarted at this situation there is only server that it will encounter downtime . we need to have more than one server

- Cannot scale if too much incoming traffic:

If the website experiences a sudden surge in traffic, a single server may not be able to handle the increased load efficiently, leading to performance issues or downtime. Scaling resources to accommodate growth would be challenging in this setup.

To address these issues, we could implement solutions such as load balancing, redundancy, and horizontal scaling to improve reliability, minimize downtime, and handle increased traffic more effectively.
