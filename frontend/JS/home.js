window.onload = () => {
    //Check if user is logged in
    if(sessionStorage.getItem('username')==null){
        window.location.href = "index.html";
    }

    //Send request for getting the posts
    $.post('http://127.0.0.1:8000/post/getPosts',{'username' : `${sessionStorage.getItem('username')}`},appendPosts);

}

function appendPosts(response) {
    let s = "";
    for(let i = 0; i < response.length;i++){
        if(response[i].image==null){
            s += `<div class="card col-sm-12 col-12" style="margin:10px">
            <div class="card-body">
            <h5 class="card-title">${response[i].title} @ ${response[i].username.username}</h5>
                <p class="card-text">${response[i].description}</p>
                <button class="btn btn-primary" onClick="likebutton(${response[i].id})">Like</button>
                <button class="btn btn-primary" onClick="commentbutton(${response[i].id})">Comment</button>
            </div>
        </div>`
        }
        else{
            s += `<div class="card col-sm-12 col-md-5" style="margin:10px">
            <div class="card-body">
            <img class="card-img-top" src="${response[i].image}">
                <h5 class="card-title">${response[i].title} @ ${response[i].username.username}</h5>
                <p class="card-text">${response[i].description}</p>
                <button class="btn btn-primary" onClick="likebutton(${response[i].id})">Like</button>
                <button class="btn btn-primary" onClick="commentbutton(${response[i].id})">Comment</button>
            </div>
        </div>`
        }
    }
    $('.post').append(s);
}

function likebutton(id){
    $.post('http://127.0.0.1:8000/post/like',{'username' : `${sessionStorage.getItem('username')}`,'postid' : `${id}`},(response) => {
        console.log(response);
    })
}

function commentbutton(id){
    
}