let my_dict = {
    'name': 'Jim',
    'age': 30,   
    'city': 'Kyiv'
}

let counter = 0;

while (true) {
    let user_input = prompt("Please enter the name you are searching for: ");
    
    if (my_dict['name'] === user_input) {
        console.log(`Name ${user_input} found`);
        break;
    } else {
        counter += 1;
        if (counter === 2){
            console.log("You have one more attempt");
        } else if (counter > 2) {
            console.log("No more attempts left");
            break;
        } else {
            console.log("Name not found");
        }
    }
}

//Use google chrome inspect tool console inside