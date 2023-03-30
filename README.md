# Yearning-wxwork
yeaning转发工单消息到企微机器人

因为yearning官方不支持直接推消息到企微，所以借助了阿里云的函数计算，将yeaning的推送信息接收处理再推送到企微

配置步骤

1、到阿里云的函数计算页面，先建一个服务
  ![image](https://user-images.githubusercontent.com/66998320/228772138-a7c5607c-baac-40f9-9edd-b851f1ce6900.png)
  
2、进服务里，点创建函数，按图创建
  ![image](https://user-images.githubusercontent.com/66998320/228773385-33695d74-fc37-4c50-9a15-0cb2be3b10dd.png)
  ![image](https://user-images.githubusercontent.com/66998320/228773489-f17451b2-721c-4707-8a96-67b2069f39d2.png)
  
3、![image](https://user-images.githubusercontent.com/66998320/228774509-f67b3799-afde-4a70-b625-6401a2fde265.png)

4、将阿里函数的访问地址填到yearning的webhook地址里
  ![image](https://user-images.githubusercontent.com/66998320/228774746-22532073-75d2-4a50-a8d3-00f20011e282.png)

效果：
  ![image](https://user-images.githubusercontent.com/66998320/228775218-e43fbde6-1a06-4a09-88a1-9be8cf720175.png)
  ![image](https://user-images.githubusercontent.com/66998320/228775412-464b8039-72f0-4c5f-ba40-8815840f6836.png)


  
  
  
