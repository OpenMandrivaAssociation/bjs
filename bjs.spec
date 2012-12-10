Name:		bjs
Version:	0.1.3
Release:	%mkrel 1
Summary:	3D tank battle game
License:	GPLv2
Group:		Games/Arcade
Url:		http://bjs.sourceforge.net/
Source:		http://sourceforge.net/projects/bjs/files/%{name}/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:	CEGUI0.6-devel
BuildRequires:	zlib-devel
BuildRequires:	SDL_gfx-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	freetype2-devel
BuildRequires:	pkgconfig(lua)
BuildRequires:	pkgconfig(omniORB4)
BuildRequires:	python-omniidl
BuildRequires:	openal-devel

%description
BJS is a funny arcade 3D multiplayer tank battle. It is fuly playable and
very fun in multiplayer. Of course the single player is also possible.
The goal of the game is just to create a good time for players ;-) There is
no story. You just get tank and go shooting other players. Currently we are
having 5 different tanks, 6 maps, 9 powerups and 4 weapons.

%prep
%setup -q
sed -i 's|lua5.1|lua|g' Makefile
sed -i 's|bjs.png|bjs|g' misc/bjs.desktop
sed -i 's|ActionGame|ArcadeGame|g' misc/bjs.desktop

%build
%make idl
%make

%install
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}/usr

%clean
%__rm -rf %{buildroot}

%files
%doc NEWS
%{_bindir}/*
%{_mandir}/man6/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*.desktop
%{_gamesdatadir}/%{name}



%changelog
* Sun Mar 25 2012 Andrey Bondrov <abondrov@mandriva.org> 0.1.3-1
+ Revision: 786669
- imported package bjs

