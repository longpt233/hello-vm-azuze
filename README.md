# hello-vm-azuze
test deploy on cloud 

# Component

> group bao gồm tất cả các thành phần còn lại: vm, public ip, nsg, interface, vnet

![](/images-readme/thanhphan.png)

# Virtual Machine 

> vm thì thuộc một vnet, sỏ hữu một public ip 

![](/images-readme/vm.png)

# Virtual Network

> vnet có thể config net-interface

![](/images-readme/vnet.png)

# Network interface

> interface có thể chỉ đinh tới một vm, chỉ định ip public( bật tắt kết nỗi từ network tới một public ip)

![](/images-readme/interface.png)
# Security

> open port

![](/images-readme/nsg.png)

> chú ý phải có service chạy ở port thì mới telnet tới port đó được

# Public IP 

> ip được kết nối tới một interface

![](/images-readme/ip.png)



