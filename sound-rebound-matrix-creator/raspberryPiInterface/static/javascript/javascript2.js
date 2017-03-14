function createAccountHTML(email,notifications){
	var html = " <div class='account' style='width:50vw; display:flex;flex-direction: row;'>" +
		    		"<div style='width:90%;'  onclick='clicked(this)'> " +
		        		"<div class='accountId' address='" + email + "'>Email - " + email +
		        		"</div>" +
		        	"<div>" +
		            "list current notifications" +
		        "</div>" +
		        "<i class='fa fa-angle-down' aria-hidden='true' style='text-align: center;'></i>" +
		        "<div class='accountDetails' style='display:none'>" +
		            notifications + 
		        "</div>" +
		    "</div>" +
		    "<div class='deleteButton'>" +
		        "<i class='fa fa-trash-o' aria-hidden='true' style='float:right'></i>" +
		    "</div>" +
		"</div>";
	return html;
}


function crateNotificationList (notifications)
{
	string = ""
	console.log(notifications)
	if(notifications.length != 0){
		
		for(var i =0; i < notifications.length; i++){
			string += "<p>" +
					 notifications[i].name;
			if(notifications[i].disabledNotification == true){
				string += "<span> - Disabled </span>";
			}
			string += "</p>"

		}

	}
	else{
		string = "<p>currently no notifications</p>";
	}
	return string;
}
