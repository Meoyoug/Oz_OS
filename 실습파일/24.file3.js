const fs = require("fs")

fs.readFile('number_four.txt', 'utf-8', (err, data) => {
    if(err){
        console.log('파일을 읽는 도중 에러가 발생하였습니다', err)
        return;
    }
    console.log('파일내용 : ', data)
})

// 덮어쓰기
let content = "4$$$4$$$44$$$4$"
fs.writeFile('number_four.txt', content, (err) => {
    if(err) {
        console.log('파일을 쓰는 도중 에러가 발생하였습니다', err)
        return;
    }
    console.log('파일을 수정했습니다.')
})

// 이어쓰기
content = '새로운 내용 추가'
fs.appendFile('number_four.txt', content, (err) => {
    if(err) {
        console.log('파일을 쓰는 도중 에러가 발생하였습니다', err)
        return;
    }
    console.log('파일에 이어쓰기를 완료했습니다.')
})