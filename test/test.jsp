<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>  
<%@ page import="java.util.*,javax.naming.*,java.sql.*,javax.sql.*"%>  
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">  
<html>  
<head>  
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">  
</head>  
<body>  
<%  
Context ctx = new InitialContext();          
String strLookup = "java:comp/env/jdbc/umbrella";     
DataSource ds =(DataSource) ctx.lookup(strLookup);    
Connection con = ds.getConnection();    
if (con != null){    
    out.print("success");    
}else{    
    out.print("failure");    
}           
%>  
</body>  
</html>