function likePost(divId){
	var imgsUrls=new Array('/static/posts/like_active.png','/static/posts/like.png');
	var likeDiv=document.getElementById(divId)
	var image = likeDiv.getElementsByTagName('img')[0];
	var likesNumber = likeDiv.getElementsByClassName('likes-number')[0];
	if(image.src.indexOf('like.png')>0){
		image.src=imgsUrls[0];
		likesNumber.textContent = Number.parseInt(likesNumber.textContent, 10) + 1
	}else {
		image.src=imgsUrls[1];
		likesNumber.textContent = Number.parseInt(likesNumber.textContent, 10) - 1
	}
}
