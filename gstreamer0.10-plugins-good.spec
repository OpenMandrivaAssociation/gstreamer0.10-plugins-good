%define major 0.10
%define majorminor 0.10
%define bname gstreamer0.10
%define gst_required_version 0.10.33

Summary:	GStreamer Streaming-media framework plug-ins
Name:		%{bname}-plugins-good
Version:	0.10.31
Release:	4
License:	LGPLv2+
Group:		Sound
URL:		http://gstreamer.freedesktop.org/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gst-plugins-good/0.10/gst-plugins-good-%{version}.tar.xz
# See https://bugzilla.gnome.org/show_bug.cgi?id=681491
Patch0:		gst-plugins-good-0.10.31-linux3.6.patch
#gw for the pixbuf plugin
BuildRequires:	pkgconfig(gdk-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(orc-0.4)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(theora)
BuildRequires:	pkgconfig(shout)
BuildRequires:	pkgconfig(libv4l1)
BuildRequires:	pkgconfig(libv4l2)
BuildRequires:	bzip2-devel
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(taglib)
BuildRequires:	pkgconfig(gudev-1.0)
# libtool dep:
BuildRequires:	pkgconfig(dbus-glib-1)
%ifarch %{ix86}
BuildRequires:	nasm => 0.90
%endif
BuildRequires:	valgrind
BuildRequires:	pkgconfig(check)
BuildRequires:	pkgconfig(gstreamer-plugins-base-0.10) >= %{gst_required_version}
BuildRequires:	gstreamer0.10-plugins-base
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	GConf2
#gw else the tests fail:
#https://bugzilla.gnome.org/show_bug.cgi?id=619717
BuildConflicts:	%{name} < 0.10.23
BuildConflicts:	%{bname}-plugins-bad < 0.10.19
Provides:	%{bname}-audiosrc
Provides:	%{bname}-audiosink
# some plugins moved from bad to good with release 0.10.23
Conflicts:	gstreamer0.10-plugins-bad < 0.10.19
# gw this is the default http source:
Suggests:	%{bname}-soup

%description
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plug-ins.

This package contains a set of plug-ins that are considered to have
good quality code, correct functionality, the preferred license (LGPL
for the plug-in code, LGPL or LGPL-compatible for the supporting
library). People writing elements should base their code on these
elements.

%package -n %{bname}-jack
Summary:	GStreamer plug-in for the Jack Sound Server
Group:		Sound
BuildRequires:	pkgconfig(jack)
Provides:	%{bname}-audiosrc
Provides:	%{bname}-audiosink

%description -n %{bname}-jack
Plug-in for the JACK professional sound server.

%files -n %{bname}-jack
%{_libdir}/gstreamer-%{majorminor}/libgstjack.so

%package -n %{bname}-soup
Summary:	GStreamer HTTP plugin based on libsoup
Group:		System/Libraries
Requires:	%{bname}-plugins
BuildRequires:	pkgconfig(libsoup-2.4)

%description -n %{bname}-soup
Plug-in for HTTP access based on libsoup.

%files -n %{bname}-soup
%{_libdir}/gstreamer-%{majorminor}/libgstsouphttpsrc.so

%package -n %{bname}-pulse
Summary:	Pulseaudio plugin for GStreamer
Group:		Sound
Requires:	%{bname}-plugins
BuildRequires:	pkgconfig(libpulse)

%description -n %{bname}-pulse
This is a GStreamer audio output plugin using the Pulseaudio sound server.

%files -n %{bname}-pulse
%{_libdir}/gstreamer-%{majorminor}/libgstpulse.so

### LIBDV ###
%package -n %{bname}-dv
Summary:	GStreamer DV plug-in
Group:		Video
Requires:	%{bname}-plugins
BuildRequires:	pkgconfig(libdv)

%description -n %{bname}-dv
Plug-in for digital video support using libdv.

%files -n %{bname}-dv
%{_libdir}/gstreamer-%{majorminor}/libgstdv.so

%package -n %{bname}-speex
Summary:	Gstreamer plugin for encoding and decoding Ogg Speex audio files
Group:		Sound
Requires:	%{bname}-plugins
BuildRequires:	pkgconfig(speex)

%description -n %{bname}-speex
Plug-Ins for creating and playing Ogg Speex audio files.

%files -n %{bname}-speex
%{_libdir}/gstreamer-%{majorminor}/libgstspeex.so

### RAW1394 ###
%package -n %{bname}-raw1394
Summary:	GStreamer raw1394 Firewire plug-in
Group:		System/Libraries
Requires:	%{bname}-plugins
BuildRequires:	pkgconfig(libavc1394)
BuildRequires:	pkgconfig(libraw1394)
BuildRequires:	pkgconfig(libiec61883)

%description -n %{bname}-raw1394
Plug-in for digital video support using raw1394.

%files -n %{bname}-raw1394
%{_libdir}/gstreamer-%{majorminor}/libgst1394.so

### FLAC ###
%package -n %{bname}-flac
Summary:	GStreamer plug-in for FLAC lossless audio
Group:		Sound
Requires:	%{bname}-plugins
BuildRequires:	pkgconfig(flac)

%description -n %{bname}-flac
Plug-in for the free FLAC lossless audio format.

%files -n %{bname}-flac
%{_libdir}/gstreamer-%{majorminor}/libgstflac.so

### ESD ###
%package -n %{bname}-esound
Summary:	Gstreamer plugin for ESD sound output
Group:		Sound
Obsoletes:	%{bname}-esd < %{version}-%{release}
Provides:	%{bname}-esd = %{version}-%{release}
Requires:	esound >= 0.2.8
BuildRequires:	pkgconfig(esound)
Requires:	%{bname}-plugins
Provides:	%{bname}-audiosrc
Provides:	%{bname}-audiosink

%description -n %{bname}-esound
Output plugin for GStreamer for use with the esound package

%files -n %{bname}-esound
%{_libdir}/gstreamer-%{majorminor}/libgstesd.so

### AALIB ###
%package -n %{bname}-aalib
Summary:	Gstreamer plugin for Ascii-art output
Group:		Video
BuildRequires:	aalib-devel >= 1.3
Requires:	%{bname}-plugins

%description -n %{bname}-aalib
Plugin for viewing movies in Ascii-art using aalib library.

%files -n %{bname}-aalib
%{_libdir}/gstreamer-%{majorminor}/libgstaasink.so

%package -n %{bname}-caca
Summary:	Gstreamer plugin for Ascii-art output
Group:		Video
BuildRequires:	pkgconfig(caca)
Requires:	%{bname}-plugins

%description -n %{bname}-caca
Plugin for viewing movies in Ascii-art using caca library.

%files -n %{bname}-caca
%{_libdir}/gstreamer-%{majorminor}/libgstcacasink.so

%package -n %{bname}-wavpack
Summary:	Gstreamer plugin for encoding and decoding WavPack audio files
Group:		Sound
Requires:	%{bname}-plugins
BuildRequires:	pkgconfig(wavpack)

%description -n %{bname}-wavpack
Plug-Ins for creating and playing WavPack audio files.

%files -n %{bname}-wavpack
%{_libdir}/gstreamer-%{majorminor}/libgstwavpack.so


%prep
%setup -q -n gst-plugins-good-%{version}
%patch0 -p1

%build
%configure2_5x  \
  --with-package-name='ROSA %{name} package' \
  --with-package-origin='http://rosalinux.com' \
  --disable-dependency-tracking   --enable-experimental --disable-hal
%make

%install
GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std GETTEXT_PACKAGE=gst-plugins-good-%{majorminor}
%find_lang gst-plugins-good-%{majorminor}
# Clean out files that should not be part of the rpm.
# This is the recommended way of dealing with it for RH8
rm -f %{buildroot}%{_libdir}/gstreamer-%{majorminor}/*.la
rm -f %{buildroot}%{_libdir}/gstreamer-%{majorminor}/*.a
rm -f %{buildroot}%{_libdir}/*.a

#blino remove development doc since we don't ship devel files
rm -rf %{buildroot}%{_docdir}/docs/plugins/html

%define schemas gstreamer-0.10

%post

%post_install_gconf_schemas %{schemas}

%preun

%preun_uninstall_gconf_schemas %{schemas}

%files -f gst-plugins-good-%{majorminor}.lang
%doc AUTHORS COPYING README NEWS
%{_sysconfdir}/gconf/schemas/gstreamer-%{majorminor}.schemas
%{_libdir}/gstreamer-%{majorminor}/libgstalaw.so
%{_libdir}/gstreamer-%{majorminor}/libgstannodex.so
%{_libdir}/gstreamer-%{majorminor}/libgstalpha.so
%{_libdir}/gstreamer-%{majorminor}/libgstalphacolor.so
%{_libdir}/gstreamer-%{majorminor}/libgstapetag.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudiofx.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudioparsers.so
%{_libdir}/gstreamer-%{majorminor}/libgstauparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstautodetect.so
%{_libdir}/gstreamer-%{majorminor}/libgstavi.so
%{_libdir}/gstreamer-%{majorminor}/libgstcairo.so
%{_libdir}/gstreamer-%{majorminor}/libgstcutter.so
%{_libdir}/gstreamer-%{majorminor}/libgstdebug.so
%{_libdir}/gstreamer-%{majorminor}/libgstdeinterlace.so
%{_libdir}/gstreamer-%{majorminor}/libgstefence.so
%{_libdir}/gstreamer-%{majorminor}/libgsteffectv.so
%{_libdir}/gstreamer-%{majorminor}/libgstflv.so
%{_libdir}/gstreamer-%{majorminor}/libgstequalizer.so
%{_libdir}/gstreamer-%{majorminor}/libgstflxdec.so
%{_libdir}/gstreamer-%{majorminor}/libgstgconfelements.so
%{_libdir}/gstreamer-%{majorminor}/libgstgdkpixbuf.so
%{_libdir}/gstreamer-%{majorminor}/libgstgoom.so
%{_libdir}/gstreamer-%{majorminor}/libgstgoom2k1.so
%{_libdir}/gstreamer-%{majorminor}/libgsticydemux.so
%{_libdir}/gstreamer-%{majorminor}/libgstid3demux.so
%{_libdir}/gstreamer-%{majorminor}/libgstimagefreeze.so
%{_libdir}/gstreamer-%{majorminor}/libgstinterleave.so
%{_libdir}/gstreamer-%{majorminor}/libgstisomp4.so
%{_libdir}/gstreamer-%{majorminor}/libgstjpeg.so
%{_libdir}/gstreamer-%{majorminor}/libgstlevel.so
%{_libdir}/gstreamer-%{majorminor}/libgstmatroska.so
%{_libdir}/gstreamer-%{majorminor}/libgstmonoscope.so
%{_libdir}/gstreamer-%{majorminor}/libgstmulaw.so
%{_libdir}/gstreamer-%{majorminor}/libgstmultifile.so
%{_libdir}/gstreamer-%{majorminor}/libgstmultipart.so
%{_libdir}/gstreamer-%{majorminor}/libgstnavigationtest.so
%{_libdir}/gstreamer-%{majorminor}/libgstossaudio.so
%{_libdir}/gstreamer-%{majorminor}/libgstoss4audio.so
%{_libdir}/gstreamer-%{majorminor}/libgstpng.so
%{_libdir}/gstreamer-%{majorminor}/libgstreplaygain.so
%{_libdir}/gstreamer-%{majorminor}/libgstrtp.so
%{_libdir}/gstreamer-%{majorminor}/libgstrtpmanager.so
%{_libdir}/gstreamer-%{majorminor}/libgstrtsp.so
%{_libdir}/gstreamer-%{majorminor}/libgstshapewipe.so
%{_libdir}/gstreamer-%{majorminor}/libgstshout2.so
%{_libdir}/gstreamer-%{majorminor}/libgstsmpte.so
%{_libdir}/gstreamer-%{majorminor}/libgstspectrum.so
%{_libdir}/gstreamer-%{majorminor}/libgsttaglib.so
%{_libdir}/gstreamer-%{majorminor}/libgstudp.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideo4linux2.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideobox.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideocrop.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideofilter.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideomixer.so
%{_libdir}/gstreamer-%{majorminor}/libgstwavenc.so
%{_libdir}/gstreamer-%{majorminor}/libgstwavparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstximagesrc.so
%{_libdir}/gstreamer-%{majorminor}/libgsty4menc.so
%dir %{_datadir}/gstreamer-%{majorminor}/
%dir %{_datadir}/gstreamer-%{majorminor}/presets
%{_datadir}/gstreamer-%{majorminor}/presets/*

%changelog
* Fri Jun 15 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 0.10.31-1
- Update to 0.10.31
- Spec cosmetics

* Thu Jul 07 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.10.30-2mdv2011.0
+ Revision: 689257
- drop dependency on pulseuadio for pulse sub-package

* Thu Jun 16 2011 Götz Waschk <waschk@mandriva.org> 0.10.30-1
+ Revision: 685485
- new version
- xz tarball from gnome FTP

* Wed May 11 2011 Funda Wang <fwang@mandriva.org> 0.10.29-1
+ Revision: 673433
- update file list
- update file list
- br gconf2
- new verison 0.10.29

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

* Tue Mar 08 2011 Götz Waschk <waschk@mandriva.org> 0.10.28-1
+ Revision: 642958
- really disable hal build
- new version

* Thu Mar 03 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.10.27-2
+ Revision: 641529
- removed hal-devel as a BR

* Sat Jan 22 2011 Götz Waschk <waschk@mandriva.org> 0.10.27-1
+ Revision: 632320
- new version
- drop patch
- bump gstreamer dep
- move jack element here

* Tue Dec 07 2010 Colin Guthrie <cguthrie@mandriva.org> 0.10.26-3mdv2011.0
+ Revision: 614207
- Fix a problem with pulsesink that causes crackling (esp. noticable on short samples e.g. event sounds on KDE)

* Thu Dec 02 2010 Götz Waschk <waschk@mandriva.org> 0.10.26-2mdv2011.0
+ Revision: 604713
- rebuild
- new version
- bump gstreamer dep
- drop patch 3

  + Maarten Vanraes <alien@mandriva.org>
    - fix alphacolor transparency passthrough

* Fri Nov 05 2010 Funda Wang <fwang@mandriva.org> 0.10.25-3mdv2011.0
+ Revision: 593587
- rebuild for gstreamer provides

* Fri Sep 03 2010 Götz Waschk <waschk@mandriva.org> 0.10.25-1mdv2011.0
+ Revision: 575668
- new version
- drop patch 1

* Tue Aug 17 2010 Colin Guthrie <cguthrie@mandriva.org> 0.10.24-5mdv2011.0
+ Revision: 570685
- Disable upstream proposed multi-threading patch as it seems to break more than it fixes.

* Mon Aug 16 2010 Colin Guthrie <cguthrie@mandriva.org> 0.10.24-4mdv2011.0
+ Revision: 570307
- Try to solve bgo#624338. This may also affect bko#232068 (hopefully)

* Thu Aug 05 2010 Colin Guthrie <cguthrie@mandriva.org> 0.10.24-3mdv2011.0
+ Revision: 566140
- Apply upstream fix for thread safety with pulsesink (bgo#624338, bko#246141)

* Sat Jul 17 2010 Götz Waschk <waschk@mandriva.org> 0.10.24-2mdv2011.0
+ Revision: 554537
- rebuild for missing source package
- new version
- bump gstreamer dep
- replace dep on liboil by orc

* Sat Jul 10 2010 Götz Waschk <waschk@mandriva.org> 0.10.23-1mdv2011.0
+ Revision: 550257
- new version
- add build conflicts with older versions
- update conflict with -bad package
- remove gamma, videobalance, videoflip elements
- add imagefreeze, oss4audio, videofilter elements

* Wed Apr 28 2010 Götz Waschk <waschk@mandriva.org> 0.10.22-1mdv2010.1
+ Revision: 540040
- new version
- bump gstreamer dep

* Tue Mar 09 2010 Götz Waschk <waschk@mandriva.org> 0.10.21-1mdv2010.1
+ Revision: 516849
- update to new version 0.10.21

* Sun Mar 07 2010 Götz Waschk <waschk@mandriva.org> 0.10.19-2mdv2010.1
+ Revision: 515602
- update conflict with -bad plugins

* Sun Mar 07 2010 Götz Waschk <waschk@mandriva.org> 0.10.19-1mdv2010.1
+ Revision: 515586
- new version
- bump deps
- update file list

* Thu Feb 11 2010 Funda Wang <fwang@mandriva.org> 0.10.18-1mdv2010.1
+ Revision: 504214
- New version 0.10.18

* Sun Jan 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.10.17-2mdv2010.1
+ Revision: 488760
- rebuilt against libjpeg v8

* Sat Nov 21 2009 Götz Waschk <waschk@mandriva.org> 0.10.17-1mdv2010.1
+ Revision: 467802
- new version
- drop pulseaudio patches

* Sun Oct 18 2009 Colin Guthrie <cguthrie@mandriva.org> 0.10.16-3mdv2010.0
+ Revision: 458097
- Backport upstream pulse changes. Fixes mdv#53554

* Fri Sep 25 2009 Olivier Blin <oblin@mandriva.com> 0.10.16-2mdv2010.0
+ Revision: 449050
- disable testsuite on mips due to timeouts (from Arnaud Patard)
- disable valgrind on mips & arm (from Arnaud Patard)

* Sun Aug 30 2009 Götz Waschk <waschk@mandriva.org> 0.10.16-1mdv2010.0
+ Revision: 422366
- new version
- update file list
- drop patch
- update conflict with bad plugins

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuilt against libjpeg v7

* Sun Jun 21 2009 Frederik Himpe <fhimpe@mandriva.org> 0.10.15-2mdv2010.0
+ Revision: 387695
- Add upstream patch fixing CVE-2009-1932

* Thu May 21 2009 Götz Waschk <waschk@mandriva.org> 0.10.15-1mdv2010.0
+ Revision: 378302
- new version
- update file list
- bump conflict with gstreamer0.10-plugins-bad

* Fri Feb 20 2009 Götz Waschk <waschk@mandriva.org> 0.10.14-1mdv2009.1
+ Revision: 343225
- new version
- drop all patches
- update file list

* Sun Feb 08 2009 Colin Guthrie <cguthrie@mandriva.org> 0.10.13-3mdv2009.1
+ Revision: 338493
- Upgrade the pulse plugin to the git master version (rewrite with stability fixes)

* Wed Jan 28 2009 Götz Waschk <waschk@mandriva.org> 0.10.13-2mdv2009.1
+ Revision: 334958
- patch memleak in pulse plugin
- remove build workaround

* Fri Jan 23 2009 Götz Waschk <waschk@mandriva.org> 0.10.13-1mdv2009.1
+ Revision: 332723
- update build deps
- fix test
- fix installation
- new version
- rediff patch 1
- drop patch 2
- fix build

* Mon Jan 19 2009 Frederic Crozat <fcrozat@mandriva.com> 0.10.11-3mdv2009.1
+ Revision: 331237
- Patch2 (CVS): fix pulseaudio memleak (GNOME bug #567746)
- Update buildrequires
- ensure autogen is called in noconfigure mode

* Sun Dec 28 2008 Funda Wang <fwang@mandriva.org> 0.10.11-2mdv2009.1
+ Revision: 320384
- rebuild for new raw1394

* Mon Nov 03 2008 Götz Waschk <waschk@mandriva.org> 0.10.11-1mdv2009.1
+ Revision: 299407
- new version
- drop patch 0
- update patch 1
- update build deps

* Tue Oct 14 2008 Götz Waschk <waschk@mandriva.org> 0.10.10-3mdv2009.1
+ Revision: 293583
- fix autogen call

* Mon Sep 01 2008 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 0.10.10-2mdv2009.0
+ Revision: 278574
- Add BuildRequires for gettext-devel (needed after starting using
  autogen.sh in previous change).
- Added libv4l support, needed by gspcav2 on linux 2.6.27
  (Patch from http://bugzilla.gnome.org/show_bug.cgi?id=545033#c7)

* Mon Sep 01 2008 Götz Waschk <waschk@mandriva.org> 0.10.10-1mdv2009.0
+ Revision: 278411
- new version
- remove cdio element

* Thu Aug 07 2008 Frederic Crozat <fcrozat@mandriva.com> 0.10.9-3mdv2009.0
+ Revision: 266433
- Patch0: ensure translated strings are in UTF-8 (GNOME bug #546822)

* Mon Aug 04 2008 Götz Waschk <waschk@mandriva.org> 0.10.9-2mdv2009.0
+ Revision: 263058
- bump
- new version
- drop patch
- add pulseaudio plugin
- move some plugins from -bad and update conflict
- reenable checks

* Tue Jul 15 2008 Götz Waschk <waschk@mandriva.org> 0.10.8-3mdv2009.0
+ Revision: 235888
- update license
- suggest soup package

* Fri May 09 2008 Götz Waschk <waschk@mandriva.org> 0.10.8-2mdv2009.0
+ Revision: 205267
- fix default audio sink

* Fri May 09 2008 Götz Waschk <waschk@mandriva.org> 0.10.8-1mdv2009.0
+ Revision: 204901
- new version
- drop patch
- move soup plugin here
- add goom2k1 plugin

* Sun May 04 2008 Götz Waschk <waschk@mandriva.org> 0.10.7-4mdv2009.0
+ Revision: 201188
- P0: security fix for CVE-2008-1686

* Thu Mar 13 2008 Götz Waschk <waschk@mandriva.org> 0.10.7-3mdv2008.1
+ Revision: 187337
- add Mandriva branding

* Mon Mar 10 2008 Frederic Crozat <fcrozat@mandriva.com> 0.10.7-2mdv2008.1
+ Revision: 183328
- Fix conflicts to handle 2008.0 upgrade

* Thu Feb 21 2008 Götz Waschk <waschk@mandriva.org> 0.10.7-1mdv2008.1
+ Revision: 173578
- new version
- update file list

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Sep 20 2007 Olivier Blin <oblin@mandriva.com> 0.10.6-3mdv2008.0
+ Revision: 91471
- remove development doc since we don't ship devel files

* Thu Aug 16 2007 Götz Waschk <waschk@mandriva.org> 0.10.6-2mdv2008.0
+ Revision: 64240
- add experimental plugins

* Wed Jun 20 2007 Götz Waschk <waschk@mandriva.org> 0.10.6-1mdv2008.0
+ Revision: 41845
- new version
- drop patch
- move wavpack plugin here
- update file list

* Wed Jun 06 2007 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 0.10.5-3mdv2008.0
+ Revision: 36088
- Rebuild with libslang2.


* Sun Apr 01 2007 Frederic Crozat <fcrozat@mandriva.com> 0.10.5-2mdv2007.1
+ Revision: 150132
- Install gconf schemas
- Don't run make check when generating package, broken ATM

* Sat Dec 30 2006 Götz Waschk <waschk@mandriva.org> 0.10.5-1mdv2007.1
+ Revision: 102876
- new version
- rediff the flac patch
- update buildrequires
- reenable checks
- update file list
- add docs
- split out caca to separate package

* Mon Dec 11 2006 Götz Waschk <waschk@mandriva.org> 0.10.4-3mdv2007.1
+ Revision: 95054
- Import gstreamer0.10-plugins-good

* Mon Dec 11 2006 Götz Waschk <waschk@mandriva.org> 0.10.4-3mdv2007.1
- patch for new flac
- fix for new caca
- add support for checks but don't enable them

* Thu Aug 17 2006 Götz Waschk <waschk@mandriva.org> 0.10.4-2mdv2007.0
- add missing buildrequires (spturtle)

* Tue Aug 15 2006 Götz Waschk <waschk@mandriva.org> 0.10.4-1mdv2007.0
- bump deps
- New release 0.10.4

* Wed Aug 02 2006 Frederic Crozat <fcrozat@mandriva.com> 0.10.3-3mdv2007.0
- Rebuild with latest dbus

* Sun Jun 18 2006 Götz Waschk <waschk@mandriva.org> 0.10.3-2mdv2007.0
- add hal module
- fix buildrequires

* Tue May 09 2006 Götz Waschk <waschk@mandriva.org> 0.10.3-1mdk
- update file list
- New release 0.10.3

* Sat Mar 18 2006 Götz Waschk <waschk@mandriva.org> 0.10.2-3mdk
- rebuild for new cdio

* Thu Feb 16 2006 Götz Waschk <waschk@mandriva.org> 0.10.2-2mdk
- fix buildrequires

* Mon Feb 13 2006 Götz Waschk <waschk@mandriva.org> 0.10.2-1mdk
- update file list
- bump deps
- New release 0.10.2

* Tue Jan 17 2006 Götz Waschk <waschk@mandriva.org> 0.10.1-1mdk
- update file list
- New release 0.10.1

* Thu Dec 29 2005 Götz Waschk <waschk@mandriva.org> 0.10.0-2mdk
- improve description
- fix buildrequires

* Tue Dec 06 2005 Götz Waschk <waschk@mandriva.org> 0.10.0-1mdk
- initial package

