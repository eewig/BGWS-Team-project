function likePost(post_id){
	var imgsUrls=new Array('/static/posts/like_active.png','/static/posts/like.png');
	var likeDiv=document.getElementById("likes-" + post_id);
	var image = likeDiv.getElementsByTagName('img')[0];
	var likesNumber = likeDiv.getElementsByClassName('likes-number')[0];

	const baseUrl = location.origin + "/like/" + post_id + "?" + "like="
	// var xhr = new XMLHttpRequest();
	// xhr.open("GET", yourUrl, true);
	// // xhr.setRequestHeader('Content-Type', 'application/json');
	// xhr.send(JSON.stringify({
	//     value: value
	// }));

	
	if(image.src.indexOf('like.png')>0){
		fetch(baseUrl + "true")
		.then(function(response) {

			return response.json();
		})
		.then(function(jsonResponse) {
			console.log(jsonResponse);
			if (jsonResponse['ok'] == "true"){
				image.src=imgsUrls[0];
				likesNumber.textContent = Number.parseInt(likesNumber.textContent, 10) + 1;
			}
		});
		}else {
			fetch(baseUrl + "false")
			.then(function(response) {
				return response.json();
			})
			.then(function(jsonResponse) {
				console.log(jsonResponse);
				if (jsonResponse['ok'] == "true"){
					image.src=imgsUrls[1];
					likesNumber.textContent = Number.parseInt(likesNumber.textContent, 10) - 1;
				}
			});
			
		}
}
