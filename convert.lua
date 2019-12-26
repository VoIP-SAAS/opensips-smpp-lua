#!/usr/bin/lua
function arg_function(str)
        local msg = tostring(AVP_get("msg"))
        local tool = tostring(AVP_get("tool"))
        local format = tostring(AVP_get("format"))
        if tool == "test" then
                xlog(tool .. ":" .. msg .. "\n")
                local handle = io.popen("python3 /etc/opensips/scripts/gsm_utf.py " .. "'" ..msg.. "'" .. " "..tool)
                local cmd_var = handle:read("*all")
                handle:close()
                xlog("Tested string ~> " .. cmd_var .. "\n")
                return AVP_set("test-str", cmd_var)
        else
                xlog(tool .. ":" .. format .. ":" .. msg .. "\n");
                local handle = io.popen("python3 /etc/opensips/scripts/gsm_utf.py " .. "'"..msg.. "'" .." "..tool.." "..format)
                local cmd_var = handle:read("*all")
                handle:close()
                xlog("Formated string ~> " .. cmd_var .. "\n")
                return AVP_set("formatted-msg", cmd_var)
        end
end
