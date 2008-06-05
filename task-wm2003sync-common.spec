Name:		task-wm2003sync-common
Version:	1.0
Release:	%{mkrel 1}
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
Requires:	kdepim-kitchensync
Requires:	synce-trayicon

%description -n task-wm2003sync-kde
This package is a meta-package for connecting with Windows Mobile 2003
and earlier devices. It depends on all packages necessary for setting
up a basic connection to the device and packages that are useful for
synchronizing with KDE applications.  At present it also suggests the
synce-trayicon package, even though this is a GTK+-based application,
as it is the only application currently capable of graphically
configuring partnerships on these devices.

%package -n task-wm2003sync-gnome
Summary:	GNOME metapackage for Windows Mobile 2003 and earlier
Group:		Communications
Requires:	task-wm2003sync-common
Requires:	libopensync-plugin-evolution2
Requires:	multisync-gui
Requires:	synce-trayicon

%description -n task-wm2003sync-gnome
This package is a meta-package for connecting with Windows Mobile 2003
and earlier devices. It depends on all packages necessary for setting
up a basic connection to the device and packages that are useful for
synchronizing with GNOME applications.

%files

%files -n task-wm2003sync-kde

%files -n task-wm2003sync-gnome

