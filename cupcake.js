
getCupcakes();

$("form").on("submit", async function(e){
    e.preventDefault();

    if($("#image").val() == ""){
        $("#image").val("https://thestayathomechef.com/wp-content/uploads/2017/12/Most-Amazing-Chocolate-Cupcakes-1-small.jpg");
    }

    const cupcake = {
        "flavor": $("#flavor").val(),
        "size": $("#size").val(),
        "rating": $("#rating").val(),
        "image": $("#image").val()
    }

    await axios.post("/api/cupcakes", cupcake);
    $("ul").append(`<li>${$("#flavor").val()}</li>`);

    $("#flavor").val("");
    $("#size").val("");
    $("#rating").val("");
    $("#image").val("");
})

async function getCupcakes(){
    const resp = await axios.get("/api/cupcakes");
    
    for(let cupcake of resp.data){
        $("ul").append(`<li>${cupcake.flavor}</li>`);
    }
}
