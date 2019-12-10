# opensips-smpp-lua
Opensips lua script to handle encoding/decoding for proto smpp
Supports: UTF16BE UTF16LE UTF16 GSM7

Opensips cfg example

```                        
                        # avp formatted-msg set in lua
                        if($fU=~"^[0-9]{1,6}$") {
                            xlog("SMS encode UTF16 with body $rb\n");
                            $avp(msg)= $rb;
                            $avp(tool) = "encode";
                            $avp(format) = "UTF16BE";

                        if($rU=~"%") {
                            $var(num-dst) = $(rU{s.select,0,%});
                        } else {
                            $var(num-dst) = $rU;
                        }
                        
                        if(lua_exec("arg_function")) {
                                xlog("Encoded body to UTF-16 ~> [$avp(formatted-msg)]\n");
                        }
                        xlog("SMS from $fU to $var(num-dst) with body $avp(formatted-msg)\n");
                        remove_body_part("text/plain");
                        add_body_part("$avp(formatted-msg)", "text/plain; charset=UTF-16");
                      }
 ```
