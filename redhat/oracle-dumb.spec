
Summary   :  Provides dependencies for an `oracle-dba'.
Summary(ru_RU.UTF-8)   : Обеспечивает разрешение зависимостей для пактов `oracle-dba'.
Name      : oracle-dumb
Version   : 1.0
Release   : 1
Group     : Database

Packager  : Kryazhevskikh Sergey, <soliverr@gmail.com>
License   : GPLv2

BuildArch : noarch
Provides  : oracle-client, oracle-server

Source: %name-%version.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}

%description
This package need to provide package dependencies to build or install
a bunch of `oracle-dba' packages.
.
Install this package if you want to use `oracle-dba' packages and already
had installed an Oracle RDBMS or Oracle client software by the official way
(Oracle Universal Installer).

%description -l ru_RU.UTF-8
Данный пакет обеспечивает разрешение зависимостей при создании или установке
пакетов `oracle-dba'.
.
Установите данный пакет, если Вы решили использовать другие пакеты `oracle-dba'
и у Вас уже установлено ПО СУБД Oracle или клиент Oracle типовым способом
с помощью Oracle Universal Installer.

%prep

%setup -q

%build

%install

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README

%changelog
* Thu Nov 6 2014 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-1  10:32:07 +0500
- Initial version of package
