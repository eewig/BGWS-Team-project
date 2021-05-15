async function likePost(post_id){
	var imgsUrls=new Array('/static/posts/like_active.png','/static/posts/like.png');
	var likeDiv=document.getElementById("likes-" + post_id);
	var image = likeDiv.getElementsByTagName('img')[0];
	var likesNumber = likeDiv.getElementsByClassName('likes-number')[0];
	const baseUrl = location.origin + "/like/" + post_id + "?" + "like="

	if(image.src.indexOf('like.png') > 0){
		const response = await fetch(baseUrl + "true");
		if (response.url.indexOf("/users/login/")>0){
			window.location.replace(response.url);
		}
		else{
			const jsonResponse = await response.json();
			if (jsonResponse['ok'] == "true"){
				image.src=imgsUrls[0];
				likesNumber.textContent = Number.parseInt(likesNumber.textContent, 10) + 1;
			}
		}
	}else {
		fetch(baseUrl + "false")
		.then(function(response) {
			return response.json();
		})
		.then(function(jsonResponse) {
			if (jsonResponse['ok'] == "true"){
				image.src=imgsUrls[1];
				likesNumber.textContent = Number.parseInt(likesNumber.textContent, 10) - 1;
			}
		});
			
	}
}
