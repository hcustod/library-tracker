// target the button with a getElementById

const submitButton = document.getElementById("submit-button");
const bookDisplay = document.getElementById("book-display");

submitButton.addEventListener("click", (event) => {
    event.preventDefault(); // prevent default form submission behav. 

    // make AJAX request to Flask backend using fetch

    fetch("/add_book", {
        method: "POST",
        body: new FormData(document.getElementById("book-form"))
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
    })
    .catch(error => {
        console.error(error);
    });

    fetch("/get_books")
    .then(response => response.json())
    .then(data => {
        let booksText = "Books in the collection: \n";
        data.forEach(book => {
            booksText += `${book.name} by ${book.author} (${book.year}) - Genre: ${book.genre}, Rating: ${book.rating}/10\n`;
        });
        bookDisplay.textContent = booksText;
    })
    .catch(error => console.error(error)); 
});