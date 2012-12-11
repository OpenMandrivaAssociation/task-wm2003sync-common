Name:		task-wm2003sync-common
Version:	1.1
Release:	%mkrel 1
Summary:	Metapackage for Windows Mobile 2003 and earlier devices
Group:		Communications
License:	GPLv2+
Requires:	synce-hal
Requires:	libopensync-plugin-synce
# For command-line partnership creation: synce-matchmaker is in librra
# - AdamW 2008/06
Suggests:	librra
Suggests:	libopensync-plugin-file
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
This package is a meta-package for connecting with Windows Mobile 2003
and earlier devices. It depends on all packages necessary for setting
up a basic connection to the device. It is not recommended that you
install this package directly, but rather that you install
task-wm2003sync-gnome or task-wm2003sync-kde, depending on your
preferred desktop environment.

%package -n task-wm2003sync-kde
Summary:	KDE metapackage for Windows Mobile 2003 and earlier
Group:		Communications
Requires:	task-wm2003sync-common
Requires:	libopensync-plugin-kdepim
Requires:	synce-kpm
#Requires:	synce-trayicon
Suggests:	kde4-kio-rapip

%description -n task-wm2003sync-kde
This package is a meta-package for connecting with Windows Mobile 2003
and earlier devices. It depends on all packages necessary for setting
up a basic connection to the device and packages that are useful for
synchronizing with KDE applications.  At present it also suggests the
synce-trayicon package, even though this is a GTK+-based application,
as it is the only application currently capable of graphically
configuring partnerships on these devices. It also depends on a
package that will allow you to access the filesystem on your Windows
Mobile device from KDE applications like Konqueror. This package is
mainly intended for use with KDE 3, as synchronization with KDE 4's
PIM applications is not yet possible. If you wish to use as much
functionality as is currently available in KDE 4, install this package
with urpmi's --no-suggests parameter, and then install the
kde4-kio-rapip package.

%package -n task-wm2003sync-gnome
Summary:	GNOME metapackage for Windows Mobile 2003 and earlier
Group:		Communications
Requires:	task-wm2003sync-common
Requires:	libopensync-plugin-evolution2
Requires:	multisync-gui
Requires:	synce-trayicon
Suggests:	synce-gvfs

%description -n task-wm2003sync-gnome
This package is a meta-package for connecting with Windows Mobile 2003
and earlier devices. It depends on all packages necessary for setting
up a basic connection to the device and packages that are useful for
synchronizing with GNOME applications. It also depends on a package
that will allow you to access the filesystem on your Windows Mobile
device from any GVFS-compatible application (most GNOME applications).

%files

%files -n task-wm2003sync-kde

%files -n task-wm2003sync-gnome



%changelog
* Tue Aug 11 2009 Emmanuel Andry <eandry@mandriva.org> 1.1-1mdv2010.0
+ Revision: 415188
- now KDE4 compliant

* Thu Sep 04 2008 Adam Williamson <awilliamson@mandriva.org> 1.0-2mdv2009.0
+ Revision: 280251
- explain KDE package is meant for KDE 3
- depend on VFS access packages

* Thu Jun 05 2008 Adam Williamson <awilliamson@mandriva.org> 1.0-1mdv2009.0
+ Revision: 215177
- import task-wm2003sync-common


