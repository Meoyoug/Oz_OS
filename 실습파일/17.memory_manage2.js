// players가 참조하는 객체 하나, boys를 참조하는 객체 하나
let players = {
    boys :{
        Bergkamp : "Striker"
    }
}

// 마찬가지로 객체하나를 참조하는데, 그 객체가 boys를 참조함
let persons = players

// 전혀다른 대상을 가리키게됨
players = ["son", "park"]

// 이 변수가 boys 객체를 직접적으로 참조함
let human = persons.boys

// persons도 전혀다른 객체를 참조함, boys객체를 참조하던 객체의 레퍼런스 카운터가 0 이됨
persons = "persons"

// human은 null이므로 boys를 참조하는 변수들이 없음 -> 레퍼런스 카운터가 0이됨
human = null

