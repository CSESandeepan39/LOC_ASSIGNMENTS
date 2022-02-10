const express = require('express')
const app = express()

app.get('/', function (req, res) {
  res.sendFile('./views/index.html',{root: __dirname})
})

app.listen(3000)

app.get('/add-item', function (req, res) {
  res.sendFile('./views/add-item.html',{root: __dirname})
  
})
app.use((req, res) => {
  res.sendFile('./views/error.html',{root: __dirname})
  
})