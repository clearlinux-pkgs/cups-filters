#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cups-filters
Version  : 1.28.6
Release  : 67
URL      : https://www.openprinting.org/download/cups-filters/cups-filters-1.28.6.tar.bz2
Source0  : https://www.openprinting.org/download/cups-filters/cups-filters-1.28.6.tar.bz2
Summary  : Library for reading and writing cups filters
Group    : Development/Tools
License  : BSD-4-Clause GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1 MIT
Requires: cups-filters-bin = %{version}-%{release}
Requires: cups-filters-data = %{version}-%{release}
Requires: cups-filters-lib = %{version}-%{release}
Requires: cups-filters-license = %{version}-%{release}
Requires: cups-filters-man = %{version}-%{release}
Requires: cups-filters-services = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : cups-dev
BuildRequires : dejavu-fonts
BuildRequires : ghostscript-dev
BuildRequires : glib-dev
BuildRequires : gnutls-dev
BuildRequires : krb5-dev
BuildRequires : openldap-dev
BuildRequires : pkgconfig(com_err)
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(fontconfig)
BuildRequires : pkgconfig(freetype2)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(lcms2)
BuildRequires : pkgconfig(libpng)
BuildRequires : pkgconfig(poppler-cpp)
BuildRequires : pkgconfig(zlib)
BuildRequires : qpdf-dev
Patch1: 0001-fix-systemd-service-file.patch

%description
-------------------------------------------------------
Looking for compile instructions?  Read the file "INSTALL.txt"
instead...

%package bin
Summary: bin components for the cups-filters package.
Group: Binaries
Requires: cups-filters-data = %{version}-%{release}
Requires: cups-filters-license = %{version}-%{release}
Requires: cups-filters-services = %{version}-%{release}

%description bin
bin components for the cups-filters package.


%package data
Summary: data components for the cups-filters package.
Group: Data

%description data
data components for the cups-filters package.


%package dev
Summary: dev components for the cups-filters package.
Group: Development
Requires: cups-filters-lib = %{version}-%{release}
Requires: cups-filters-bin = %{version}-%{release}
Requires: cups-filters-data = %{version}-%{release}
Provides: cups-filters-devel = %{version}-%{release}
Requires: cups-filters = %{version}-%{release}

%description dev
dev components for the cups-filters package.


%package doc
Summary: doc components for the cups-filters package.
Group: Documentation
Requires: cups-filters-man = %{version}-%{release}

%description doc
doc components for the cups-filters package.


%package lib
Summary: lib components for the cups-filters package.
Group: Libraries
Requires: cups-filters-data = %{version}-%{release}
Requires: cups-filters-license = %{version}-%{release}

%description lib
lib components for the cups-filters package.


%package license
Summary: license components for the cups-filters package.
Group: Default

%description license
license components for the cups-filters package.


%package man
Summary: man components for the cups-filters package.
Group: Default

%description man
man components for the cups-filters package.


%package services
Summary: services components for the cups-filters package.
Group: Systemd services

%description services
services components for the cups-filters package.


%prep
%setup -q -n cups-filters-1.28.6
cd %{_builddir}/cups-filters-1.28.6
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1606939596
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%autogen --disable-static --disable-avahi --without-tiff --disable-ijs  --disable-mutool --without-rcdir --disable-braille --with-fontdir=/usr/share/defaults/fonts/conf.d --with-pdftops=pdftocairo --enable-driverless  --enable-auto-setup-driverless
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1606939596
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/cups-filters
cp %{_builddir}/cups-filters-1.28.6/COPYING %{buildroot}/usr/share/package-licenses/cups-filters/5a5f215ed6c3222d7b07bc84da8d6d9755d65883
%make_install
## install_append content
mkdir -p %{buildroot}/usr/lib/systemd/system
install -p -m 644 utils/cups-browsed.service %{buildroot}/usr/lib/systemd/system/cups-browsed.service
## install_append end

%files
%defattr(-,root,root,-)
/usr/lib/cups/backend/beh
/usr/lib/cups/backend/driverless
/usr/lib/cups/backend/driverless-fax
/usr/lib/cups/backend/implicitclass
/usr/lib/cups/backend/parallel
/usr/lib/cups/backend/serial
/usr/lib/cups/driver/driverless
/usr/lib/cups/driver/driverless-fax
/usr/lib/cups/filter/bannertopdf
/usr/lib/cups/filter/commandtoescpx
/usr/lib/cups/filter/commandtopclx
/usr/lib/cups/filter/foomatic-rip
/usr/lib/cups/filter/gstopdf
/usr/lib/cups/filter/gstopxl
/usr/lib/cups/filter/gstoraster
/usr/lib/cups/filter/imagetopdf
/usr/lib/cups/filter/imagetops
/usr/lib/cups/filter/imagetoraster
/usr/lib/cups/filter/pdftopdf
/usr/lib/cups/filter/pdftops
/usr/lib/cups/filter/pdftoraster
/usr/lib/cups/filter/rastertoescpx
/usr/lib/cups/filter/rastertopclm
/usr/lib/cups/filter/rastertopclx
/usr/lib/cups/filter/rastertopdf
/usr/lib/cups/filter/rastertops
/usr/lib/cups/filter/sys5ippprinter
/usr/lib/cups/filter/texttopdf
/usr/lib/cups/filter/texttops
/usr/lib/cups/filter/texttotext

%files bin
%defattr(-,root,root,-)
/usr/bin/cups-browsed
/usr/bin/driverless
/usr/bin/driverless-fax
/usr/bin/foomatic-rip
/usr/bin/ttfread

%files data
%defattr(-,root,root,-)
/usr/share/cups/banners/classified
/usr/share/cups/banners/confidential
/usr/share/cups/banners/form
/usr/share/cups/banners/secret
/usr/share/cups/banners/standard
/usr/share/cups/banners/topsecret
/usr/share/cups/banners/unclassified
/usr/share/cups/charsets/pdf.utf-8
/usr/share/cups/charsets/pdf.utf-8.heavy
/usr/share/cups/charsets/pdf.utf-8.simple
/usr/share/cups/data/classified.pdf
/usr/share/cups/data/confidential.pdf
/usr/share/cups/data/default-testpage.pdf
/usr/share/cups/data/default.pdf
/usr/share/cups/data/form_english.pdf
/usr/share/cups/data/form_english_in.odt
/usr/share/cups/data/form_russian.pdf
/usr/share/cups/data/form_russian_in.odt
/usr/share/cups/data/secret.pdf
/usr/share/cups/data/standard.pdf
/usr/share/cups/data/testprint
/usr/share/cups/data/topsecret.pdf
/usr/share/cups/data/unclassified.pdf
/usr/share/cups/drv/cupsfilters.drv
/usr/share/cups/mime/cupsfilters-ghostscript.convs
/usr/share/cups/mime/cupsfilters-poppler.convs
/usr/share/cups/mime/cupsfilters.convs
/usr/share/cups/mime/cupsfilters.types
/usr/share/cups/ppdc/escp.h
/usr/share/cups/ppdc/pcl.h
/usr/share/ppd/cupsfilters/Fuji_Xerox-DocuPrint_CM305_df-PDF.ppd
/usr/share/ppd/cupsfilters/Generic-PDF_Printer-PDF.ppd
/usr/share/ppd/cupsfilters/HP-Color_LaserJet_CM3530_MFP-PDF.ppd
/usr/share/ppd/cupsfilters/Ricoh-PDF_Printer-PDF.ppd
/usr/share/ppd/cupsfilters/pxlcolor.ppd
/usr/share/ppd/cupsfilters/pxlmono.ppd

%files dev
%defattr(-,root,root,-)
/usr/include/cupsfilters/colord.h
/usr/include/cupsfilters/colormanager.h
/usr/include/cupsfilters/driver.h
/usr/include/cupsfilters/image.h
/usr/include/cupsfilters/ipp.h
/usr/include/cupsfilters/pdftoippprinter.h
/usr/include/cupsfilters/ppdgenerator.h
/usr/include/cupsfilters/raster.h
/usr/include/fontembed/bitset.h
/usr/include/fontembed/embed.h
/usr/include/fontembed/fontfile.h
/usr/include/fontembed/iofn.h
/usr/include/fontembed/sfnt.h
/usr/lib64/libcupsfilters.so
/usr/lib64/libfontembed.so
/usr/lib64/pkgconfig/libcupsfilters.pc
/usr/lib64/pkgconfig/libfontembed.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/cups\-filters/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libcupsfilters.so.1
/usr/lib64/libcupsfilters.so.1.0.0
/usr/lib64/libfontembed.so.1
/usr/lib64/libfontembed.so.1.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cups-filters/5a5f215ed6c3222d7b07bc84da8d6d9755d65883

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/driverless.1
/usr/share/man/man1/foomatic-rip.1
/usr/share/man/man5/cups-browsed.conf.5
/usr/share/man/man8/cups-browsed.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/cups-browsed.service
