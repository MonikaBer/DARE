#!/bin/bash

declare -a id_configuration
declare -a ports=("81" "82" "83" "84")
loop_index=0
select_at_random=$1

function randomized_sleep() {
	rotation_time_sec=$(shuf -i 1-5 -n 1) # default  15-60
	printf "Sleep %d seconds\n" "$rotation_time_sec"
	sleep "$rotation_time_sec"
}

function create_configuration(){
	sudo nft add table inet dare
	sudo nft -- add chain inet dare prerouting { type nat hook prerouting priority -100 \; } 
	sudo nft add rule inet dare prerouting tcp dport 80 counter redirect to :81
	#sudo nft replace rule inet dare prerouting handle 4 tcp 
	#sudo nft add set inet dare dare_port_set { type mark \; }
}

function reset_configuration(){
	sudo nft delete table inet dare
}

function update_configuration(){
	set_to_port="$1"
	printf "Redirect tcp 80 to new port %d\n" "$set_to_port"
	sudo nft replace rule inet dare prerouting handle 2 tcp dport 80 counter redirect to :"$set_to_port"
}

function choose_port() {
	if [[ ! -z "$select_at_random" && "$select_at_random" =~ "--rand-port" ]]
	then
		local new_loop_index=$[ $RANDOM % ${#ports[@]} ]
		if [[ ! "$new_loop_index" == "$loop_index" ]]
		then
			loop_index=$((new_loop_index))
		else
			loop_index=$((new_loop_index+1))
		fi
	else
		loop_index=$((loop_index+1))
	fi

	local arr_size=${#ports[@]}
	if (( loop_index >= arr_size ))
	then
		let loop_index=0
	fi

	local new_port=${ports[$loop_index]}
	return "$new_port"
}

function service_loop(){
	printf "Started service loop\n"
	while [ 1 ]
	do
		choose_port
		local new_port="$?"
		printf "New port: %s\n" "$new_port"
		update_configuration "$new_port"
		randomized_sleep 
	done
}

function start() {
	reset_configuration
	create_configuration
	service_loop
}

start