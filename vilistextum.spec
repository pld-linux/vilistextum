Summary:	HTML to text converter
Summary(pl.UTF-8):	Konwerter z HTML-a do tekstu
Name:		vilistextum
Version:	2.6.7
Release:	1
License:	GPL v2
Group:		Applications/Text
Source0:	http://dl.sourceforge.net/vilistextum/%{name}-%{version}.tar.bz2
# Source0-md5:	e35ae3d99d1f90dd78a2a87adf1db8cf
URL:		http://bhaak.dyndns.org/vilistextum/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vilistextum is a small and fast HTML to text / ascii converter
specifically programmed to get the best out of incorrect html. It is
quite fault-tolerant and deals well with badly-formed or otherwise
quirky HTML. It is able to optimize for ebook reading, collapse
multiple blank lines, and create footnotes out of links.

%description -l pl.UTF-8
Vilistextum jest małym i szybkim narzędziem do konwersji HTML-a do
tekstu, zaprogramowanym do uzyskania najlepszej jakości przy błędnym
HTML-u. Jest odporny na błędy oraz radzi sobie ze źle formatowanym
HTML-em. Jest także zoptymalizowany do czytania ebooków, łączenia
wielu pustych linii i tworzenia stopek z odnośnikami.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES doc/*.html
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
