const server = require("express")
const app = server()
const PORT = 8077
const handle = require("express-handlebars")
const bodyParser =  require("body-parser")
const socket = require("socket.io")








app.set("view engine",'handlebars')

app.engine('handlebars',handle())

app.get("/",function(req,res){
    
})


i = "text_plain"






app.get("/api/send",(req,res)=>{
    res.render("index")})






app.listen(PORT,function(){
    console.log("server listening to " + PORT)})
