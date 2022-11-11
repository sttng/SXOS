https://gbatemp.net/threads/whats-the-challenge-with-the-xci-loader.520247/page-3

```
_hexkyz_
Oct 8, 2018
#43
Moral standpoints aside, no one will be able to replicate SX's XCI loading and distribute it as free open source software.
Not because of any technical hurdles or anything, but because it's flat out illegal.

TX reversed most of the gamecard protocol from the FS sysmodule and re-implemented it in their Loader KIP, hidden away inside a MIPS VM and a few layers of obfuscation. However, to achieve this, TX included sectors dumped from a real gamecard and the gamecard controller's certificate (which can be obtained by FS using a specific command). You can find these binaries by unpacking SX OS and searching inside the Loader KIP (simple hex editor will do) for "CERT" and "LOTUS".
Basically, any form of XCI loading requires heavily patching the FS sysmodule which can be quite a task if you want to support all firmware versions and what not. To avoid this, TX instead applies a single patch to FS which redirects gamecard commands to their MIPS VM. Then, code in their VM replies to the gamecard commands issued by FS with signed data ripped from a real gamecard.
After the authentication process has been forged, the VM is free to read data from the SD card and send it back to FS each time FS sends the gamecard sector reading command.

There are a few more details which I'm saving up for the writeup (SOON™), but that's the gist of it. A free solution will never be able to take this path for obvious reasons (instant takedown and lawsuits galore!), so a more complex approach will be necessary.
```

https://switchbrew.org/wiki/Lotus3

https://gbatemp.net/threads/hack-sxos.582831/page-49

https://github.com/chronoss09/Licence-SXOS-GRATUITE
