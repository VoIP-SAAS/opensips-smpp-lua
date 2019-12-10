#!/usr/bin/lua
function arg_function(str)
	local msg = tostring(AVP_get("msg"))
	local tool = tostring(AVP_get("tool"))
	local format = tostring(AVP_get("format"))
	xlog(tool .. ":" .. format .. ":" .. msg .. "\n");
	local handle = io.popen("python3 /etc/opensips/scripts/gsm_utf.py " .. "'"..msg.. "'" .." "..tool.." "..format)
	local main_string = handle:read("*all")
	handle:close()
	xlog("Formated string ~>" .. main_string .. "\n");
	return AVP_set("formatted-msg", main_string)
end
